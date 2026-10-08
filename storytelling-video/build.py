"""把 images/ 和 audio/ 里的素材合成为 9:16 竖屏短视频。
用法: python build.py  (需要 imageio-ffmpeg: pip install imageio-ffmpeg)
"""
import json, subprocess, pathlib, imageio_ffmpeg

HERE = pathlib.Path(__file__).parent
FF = imageio_ffmpeg.get_ffmpeg_exe()
story = json.loads((HERE / "story.json").read_text(encoding="utf-8"))
out_dir = HERE / "segments"
out_dir.mkdir(exist_ok=True)

clips = [(HERE / f"images/scene{s['id']}.jpg", HERE / f"audio/scene{s['id']}.mp3") for s in story["scenes"]]
clips.append((HERE / "images/scene6.jpg", HERE / "audio/ending.mp3"))  # 结尾钩子沿用最后一张画面

segs = []
for i, (img, aud) in enumerate(clips, 1):
    seg = out_dir / f"seg{i:02d}.mp4"
    subprocess.run([
        FF, "-y", "-loop", "1", "-i", str(img), "-i", str(aud),
        "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,format=yuv420p",
        "-c:v", "libx264", "-tune", "stillimage", "-r", "25",
        "-c:a", "aac", "-b:a", "128k", "-shortest", str(seg)], check=True)
    segs.append(seg)

lst = out_dir / "list.txt"
lst.write_text("".join(f"file '{s.name}'\n" for s in segs), encoding="utf-8")
final = HERE / "output" / "story_video.mp4"
final.parent.mkdir(exist_ok=True)
subprocess.run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(final)],
               check=True, cwd=out_dir)
print("written", final)
