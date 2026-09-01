#!/usr/bin/env python3
"""Build the repository social preview and illustrated workflow GIF."""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


INK = "#14213D"
BLUE = "#2459D3"
CORAL = "#EB735D"
PAPER = "#F7F2E8"
MUTED = "#5C667A"
LIGHT_BLUE = "#EAF0FF"
LIGHT_CORAL = "#FCECE7"
WHITE = "#FFFDFC"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default(size=size)


def cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    scale = max(target_w / image.width, target_h / image.height)
    resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h)).convert("RGBA")


def rounded_panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str | None = None, radius: int = 24) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=2 if outline else 1)


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    text: str,
    xy: tuple[int, int],
    width_chars: int,
    face: ImageFont.FreeTypeFont,
    fill: str,
    spacing: int = 8,
) -> int:
    lines = []
    for paragraph in text.split("\n"):
        lines.extend(wrap(paragraph, width=width_chars) or [""])
    x, y = xy
    line_height = face.getbbox("Ag")[3] - face.getbbox("Ag")[1] + spacing
    for line in lines:
        draw.text((x, y), line, font=face, fill=fill)
        y += line_height
    return y


def base_frame(background: Image.Image, size: tuple[int, int]) -> Image.Image:
    frame = cover(background, size)
    veil = Image.new("RGBA", size, (247, 242, 232, 224))
    frame = Image.alpha_composite(frame, veil)
    draw = ImageDraw.Draw(frame)
    draw.rectangle((0, 0, 10, size[1]), fill=BLUE)
    return frame


def build_social_preview(background: Image.Image, output: Path) -> None:
    canvas = cover(background, (1280, 640))
    veil = Image.new("RGBA", canvas.size, (247, 242, 232, 185))
    canvas = Image.alpha_composite(canvas, veil)
    draw = ImageDraw.Draw(canvas)

    draw.rounded_rectangle((72, 70, 330, 112), radius=21, fill=INK)
    draw.text((95, 81), "BILINGUAL AGENT SKILL", font=font(18, bold=True), fill=WHITE)
    draw.text((70, 160), "de-ai-writing", font=font(78, bold=True), fill=INK)
    draw.text((75, 264), "Natural Chinese & English writing", font=font(31), fill=INK)

    draw.line((76, 330, 710, 330), fill=BLUE, width=5)
    draw.text((75, 365), "Keep the evidence. Lose the template.", font=font(29, bold=True), fill=INK)
    draw.text((76, 424), "Sentence-level edits  •  Full-manuscript structural audits", font=font(22), fill=MUTED)

    rounded_panel(draw, (72, 510, 535, 568), fill="#FFFFFFD9", outline="#C9D4EA", radius=18)
    draw.text((96, 527), "CODEX   •   CLAUDE CODE   •   CURSOR", font=font(19, bold=True), fill=BLUE)

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(output, optimize=True, quality=94)


def frame_header(draw: ImageDraw.ImageDraw, step: str, title: str) -> None:
    draw.rounded_rectangle((42, 28, 172, 62), radius=17, fill=INK)
    draw.text((61, 36), step, font=font(15, bold=True), fill=WHITE)
    draw.text((42, 82), title, font=font(38, bold=True), fill=INK)


def build_demo(background: Image.Image, output: Path) -> None:
    size = (960, 540)
    frames: list[Image.Image] = []

    # 1 — Positioning
    image = base_frame(background, size)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((44, 40, 292, 76), radius=18, fill=INK)
    draw.text((65, 49), "ILLUSTRATED WORKFLOW", font=font(15, bold=True), fill=WHITE)
    draw.text((42, 122), "de-ai-writing", font=font(62, bold=True), fill=INK)
    draw.text((46, 210), "Natural Chinese & English writing", font=font(28), fill=INK)
    draw.line((46, 265, 650, 265), fill=BLUE, width=5)
    draw.text((46, 304), "Keep the evidence. Lose the template.", font=font(27, bold=True), fill=INK)
    rounded_panel(draw, (44, 390, 688, 465), WHITE, "#C9D4EA", 20)
    draw.text((67, 409), "Sentence  →  paragraph  →  full manuscript", font=font(24, bold=True), fill=BLUE)
    draw.text((67, 441), "No detector promises. No invented facts.", font=font(18), fill=MUTED)
    frames.append(image)

    # 2 — Before
    image = base_frame(background, size)
    draw = ImageDraw.Draw(image)
    frame_header(draw, "01  INPUT", "Start with the claim, not the polish")
    rounded_panel(draw, (42, 148, 918, 470), WHITE, "#D7DCE6")
    draw.rounded_rectangle((68, 176, 355, 212), radius=8, fill=LIGHT_CORAL)
    draw.text((79, 182), "Importantly, it is worth noting that", font=font(19, bold=True), fill=CORAL)
    before = (
        "participants who received the reminder were observed to have a lower risk of missing "
        "follow-up visits. The adjusted risk ratio was 0.74 (95% CI, 0.56–0.98) in 218 participants.\n\n"
        "This finding highlights the important role that reminders may play... Taken together, "
        "these findings suggest a potentially valuable strategy."
    )
    draw_wrapped(draw, before, (69, 231), 83, font(21), INK, spacing=9)
    draw.text((43, 496), "Synthetic example — facts are locked before rewriting", font=font(17), fill=MUTED)
    frames.append(image)

    # 3 — Diagnose
    image = base_frame(background, size)
    draw = ImageDraw.Draw(image)
    frame_header(draw, "02  DIAGNOSE", "Separate evidence from verbal padding")
    cards = [
        ((42, 158, 304, 447), "LOCK", "n = 218\nRR = 0.74\n95% CI 0.56–0.98", "Numbers and direction stay fixed", LIGHT_BLUE, BLUE),
        ((349, 158, 611, 447), "FIND", "Same conclusion\nrepeated 3 times", "Fluent restatement is not analysis", LIGHT_CORAL, CORAL),
        ((656, 158, 918, 447), "BOUND", "Association\n≠\ncausation", "Observational design sets the ceiling", "#EDF4EE", "#39714B"),
    ]
    for box, label, main, note, fill, accent in cards:
        rounded_panel(draw, box, WHITE, "#D7DCE6")
        x1, y1, _, _ = box
        draw.rounded_rectangle((x1 + 20, y1 + 20, x1 + 110, y1 + 52), radius=16, fill=fill)
        draw.text((x1 + 38, y1 + 28), label, font=font(14, bold=True), fill=accent)
        draw_wrapped(draw, main, (x1 + 22, y1 + 90), 18, font(26, bold=True), INK, spacing=8)
        draw_wrapped(draw, note, (x1 + 22, y1 + 225), 24, font(17), MUTED, spacing=7)
    frames.append(image)

    # 4 — After
    image = base_frame(background, size)
    draw = ImageDraw.Draw(image)
    frame_header(draw, "03  REWRITE", "Say exactly what the evidence supports")
    rounded_panel(draw, (42, 152, 918, 426), WHITE, "#C9D4EA")
    after = (
        "Among 218 participants, receipt of the reminder was associated with fewer missed follow-up "
        "visits (adjusted risk ratio, 0.74; 95% CI, 0.56–0.98).\n\n"
        "Because the analysis was observational, this association does not establish that the reminder caused the difference."
    )
    draw_wrapped(draw, after, (72, 190), 78, font(23), INK, spacing=12)
    draw.rounded_rectangle((42, 458, 534, 501), radius=20, fill=LIGHT_BLUE)
    draw.text((63, 469), "Same evidence  •  less repetition  •  clear limit", font=font(17, bold=True), fill=BLUE)
    frames.append(image)

    # 5 — Document-level audit
    image = base_frame(background, size)
    draw = ImageDraw.Draw(image)
    frame_header(draw, "04  SCALE UP", "Audit the architecture of long papers")
    sections = ["Abstract", "Introduction", "Limits", "Two gates", "States", "Governance", "Conclusion"]
    y = 164
    for index, section in enumerate(sections):
        color = BLUE if section in {"Abstract", "Introduction", "Two gates", "Governance", "Conclusion"} else CORAL
        draw.ellipse((64, y, 82, y + 18), fill=color)
        draw.text((99, y - 3), section, font=font(18, bold=section in {"Two gates", "Governance"}), fill=INK)
        if index < len(sections) - 1:
            draw.line((73, y + 20, 73, y + 44), fill="#A9B2C2", width=3)
        y += 48
    rounded_panel(draw, (355, 155, 910, 463), WHITE, "#D7DCE6")
    draw.text((385, 180), "THESIS-RECURRENCE MAP", font=font(16, bold=True), fill=BLUE)
    draw.text((385, 224), "boundary", font=font(25, bold=True), fill=INK)
    draw.text((535, 224), "→", font=font(25, bold=True), fill=MUTED)
    draw.text((580, 224), "gate", font=font(25, bold=True), fill=INK)
    draw.text((680, 224), "→", font=font(25, bold=True), fill=MUTED)
    draw.text((725, 224), "state", font=font(25, bold=True), fill=CORAL)
    draw.line((724, 258, 800, 258), fill=CORAL, width=3)
    draw.text((385, 293), "Keep a label only when it changes:", font=font(20), fill=INK)
    draw.text((408, 334), "evidence  •  interpretation  •  action", font=font(20, bold=True), fill=BLUE)
    draw.text((385, 391), "Compress first. Line-edit second.", font=font(22, bold=True), fill=INK)
    frames.append(image)

    # 6 — Install
    image = base_frame(background, size)
    draw = ImageDraw.Draw(image)
    draw.text((42, 52), "One skill. Three agents.", font=font(43, bold=True), fill=INK)
    draw.text((44, 112), "Codex  •  Claude Code  •  Cursor", font=font(25, bold=True), fill=BLUE)
    rounded_panel(draw, (42, 184, 918, 298), INK)
    draw.text((72, 214), "npx skills add qiyanghong2020/de-ai-writing -g", font=font(22, bold=True), fill=WHITE)
    draw.text((72, 255), "Then invoke de-ai-writing in your agent.", font=font(18), fill="#DCE5F8")
    draw.text((42, 354), "Keep the evidence.", font=font(37, bold=True), fill=INK)
    draw.text((42, 403), "Lose the template.", font=font(37, bold=True), fill=CORAL)
    draw.text((44, 476), "github.com/qiyanghong2020/de-ai-writing", font=font(18), fill=MUTED)
    frames.append(image)

    palette_frames = [frame.convert("RGB").convert("P", palette=Image.Palette.ADAPTIVE, colors=128) for frame in frames]
    output.parent.mkdir(parents=True, exist_ok=True)
    palette_frames[0].save(
        output,
        save_all=True,
        append_images=palette_frames[1:],
        duration=[5000] * len(palette_frames),
        loop=0,
        optimize=True,
        disposal=2,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--background", type=Path, default=Path("assets/social-preview-background.png"))
    parser.add_argument("--output-dir", type=Path, default=Path("assets"))
    args = parser.parse_args()

    background = Image.open(args.background)
    build_social_preview(background, args.output_dir / "social-preview.png")
    build_demo(background, args.output_dir / "demo.gif")
    print(args.output_dir / "social-preview.png")
    print(args.output_dir / "demo.gif")


if __name__ == "__main__":
    main()
