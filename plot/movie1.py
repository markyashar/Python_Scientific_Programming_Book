from scitools.std import sqrt, pi, exp, linspace, plot, movie
import time, glob, os, sys

# Clean up old frames
for name in glob.glob('tmp_*.eps'):
    os.remove(name)

def f(x, m, s):
    return (1.0/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s)**2)

m = 0
s_max = 2
s_min = 0.2
x = linspace(m -3*s_max, m + 3*s_max, 1000)
s_values = linspace(s_max, s_min, 30)
# f is max for x=m; smaller s gives larger max value
max_f = f(m, m, s_min)

# Show the movie, and make hardcopies of frames simulatenously
counter = 0
for s in s_values:
    y = f(x, m, s)
    plot(x, y, axis=[x[0], x[-1], -0.1, max_f],
         xlabel='x', ylabel='f', legend='s=%4.2f' % s,
         savefig='tmp_%04d.png' % counter)
    counter += 1
    #time.sleep(0.2)  # can insert a pause to control movie speed

if '--no-moviefile' in sys.argv:
    # Drop making movie files
    import sys; sys.exit(0)

# Make movie file the simplest possible way
movie('tmp_*.png')
import glob, os
print 'generated the file', glob.glob('movie.*')[0]
#os.remove(glob.glob('movie.*')[0])

# Make animated GIF movie in the file tmpmovie.gif
movie('tmp_*.png', encoder='convert', fps=2,
      output_file='tmpmovie.gif')

# Show movie (os.system runs an operating system command)
os.system('animate tmpmovie.gif &')

# Other formats

# HTML
movie('tmp_*.png', encoder='html', fps=3,
      output_file='tmpmovie.html')  # play in HTML file

# MPEG
movie('tmp_*.png', encoder='ppmtompeg', fps=24,
      output_file='tmpmovie1.mpeg') # requires netpbm package

# MPEG
movie('tmp_*.png', encoder='ffmpeg', fps=4,
      output_file='tmpmovie1b.mpeg') # requires ffmpeg package

# AVI
movie('tmp_*.png', encoder='ffmpeg', fps=4,
      output_file='tmpmovie1.avi') # requires ffmpeg package

# MPEG
movie('tmp_*.png', encoder='ffmpeg',
      output_file='tmpmovie1c.mpeg', vodec='mpeg2video')


# mpeg_encode is not much available nowadays...
#movie('tmp_*.png', encoder='mpeg_encode', fps=24,
#      output_file='tmpmovie3.mpeg',
#      vcodec='mpeg2video', vbitrate=2400, qscale=4)

