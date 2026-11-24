import subprocess, numpy as np, glob, os
# automated visual QA: for each scene sample frames every 1s; flag content touching the frame edge (clipping),
# long blank stretches, and report per-scene max brightness coverage.
os.chdir('/home/sprite/rh')
W, H = 480, 270
for f in sorted(glob.glob('out/*.mp4')):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', f, '-vf', 'fps=1,scale=%d:%d' % (W, H), '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W)
    bg = 16
    edge = []
    blank = 0
    for i, a in enumerate(fr):
        m = a > bg + 40
        if m.mean() < 0.002:
            blank += 1
        e = m[:3].mean() + m[-3:].mean() + m[:, :3].mean() + m[:, -3:].mean()
        if e > 0.02:
            edge.append(i)
    print(os.path.basename(f), len(fr), "blank_at", [i for i,a in enumerate(fr) if (a>56).mean()<0.002])
