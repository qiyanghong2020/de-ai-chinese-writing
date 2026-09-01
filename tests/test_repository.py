import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class SkillContractTests(unittest.TestCase):
    def test_skill_frontmatter_and_release_metadata(self):
        text = read("SKILL.md")
        self.assertTrue(text.startswith("---\n"))
        frontmatter = text.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name: de-ai-writing$")
        self.assertRegex(frontmatter, r"(?m)^description: .{80,}$")
        self.assertRegex(frontmatter, r"(?m)^license: MIT$")
        self.assertRegex(frontmatter, r'(?m)^  version: "1\.0\.1"$')

    def test_every_skill_reference_exists(self):
        references = sorted(set(re.findall(r"references/[a-z0-9_.-]+\.md", read("SKILL.md"))))
        self.assertGreaterEqual(len(references), 4)
        missing = [path for path in references if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])

    def test_core_safeguards_remain_present(self):
        skill = read("SKILL.md")
        required_fragments = [
            "Do not make the prose longer just to seem more human.",
            "Do not infer authorship or the extent of AI use from prose style.",
            "no detector-evasion claim or promise",
            "Preserve a writer's legitimate Chinese style, non-native English style, or World English variety",
            "if the request is local, do not expand it into a manuscript-wide restructure",
        ]
        for fragment in required_fragments:
            self.assertIn(fragment, skill)

    def test_document_level_audit_contract(self):
        combined = read("references/english.md") + read("references/execution-patterns.md")
        required_fragments = [
            "Cross-section semantic redundancy",
            "Repeated rhetorical closure",
            "Over-neat taxonomy",
            "Conceptual relabeling",
            "Low analytical increment",
            "Contribution-to-length imbalance",
            "Unchallenged central thesis",
            "thesis-recurrence map",
            "framework inventory",
        ]
        for fragment in required_fragments:
            self.assertIn(fragment, combined)

    def test_worked_examples_cover_required_lanes(self):
        examples = sorted((ROOT / "examples").glob("[0-9][0-9]-*.md"))
        self.assertGreaterEqual(len(examples), 6)
        combined = "\n".join(path.read_text(encoding="utf-8") for path in examples)
        for marker in [
            "English academic",
            "English workplace email",
            "中文医学",
            "中文工作邮件",
            "Long Viewpoint",
            "Taxonomy preservation",
            "World English",
        ]:
            self.assertIn(marker, combined)
        for path in examples:
            text = path.read_text(encoding="utf-8")
            self.assertTrue("Synthetic demonstration" in text or "合成演示材料" in text)

    def test_behavior_cases_have_positive_and_negative_expectations(self):
        cases = json.loads(read("tests/behavior_cases.json"))
        self.assertGreaterEqual(len(cases), 2)
        ids = {case["id"] for case in cases}
        self.assertIn("long-viewpoint-cross-section-redundancy", ids)
        self.assertIn("functional-taxonomy-negative-control", ids)
        for case in cases:
            self.assertTrue(case["expected_decisions"])
            self.assertTrue(case["forbidden_outcomes"])

    def test_plugin_submission_materials(self):
        cases = json.loads(read("tests/plugin_submission_cases.json"))
        self.assertEqual(len(cases["positive"]), 5)
        self.assertEqual(len(cases["negative"]), 3)
        for case in cases["positive"]:
            self.assertTrue(case["user_prompt"])
            self.assertTrue(case["expected_behavior"])
            self.assertTrue(case["expected_result_shape"])
            self.assertTrue(case["fixture_data"])
        for case in cases["negative"]:
            self.assertTrue(case["user_prompt"])
            self.assertTrue(case["expected_behavior"])
            self.assertTrue(case["why_not_complete"])
        for path in [
            "assets/plugin-logo.png",
            "docs/plugin-submission.md",
            "docs/privacy.md",
            "docs/terms.md",
        ]:
            self.assertTrue((ROOT / path).is_file(), path)

    def test_readme_local_links_resolve(self):
        for readme_name in ["README.md", "README.zh-CN.md"]:
            text = read(readme_name)
            targets = re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)
            targets += re.findall(r'(?:src|href)="([^"]+)"', text)
            missing = []
            for target in targets:
                target = target.split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                if not (ROOT / target).exists():
                    missing.append(target)
            self.assertEqual(missing, [], f"broken links in {readme_name}")

    def test_no_machine_specific_paths_are_published(self):
        text_files = [
            path
            for path in ROOT.rglob("*")
            if path.is_file() and ".git" not in path.parts and path.suffix in {".md", ".py", ".json", ".yml", ".yaml"}
        ]
        combined = "\n".join(path.read_text(encoding="utf-8") for path in text_files)
        forbidden_paths = ["/" + "Users/" + "a12", "/" + "home/" + "hongqy"]
        for forbidden_path in forbidden_paths:
            self.assertNotIn(forbidden_path, combined)


if __name__ == "__main__":
    unittest.main()
