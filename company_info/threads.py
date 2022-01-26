# import time
# import threading
# start=time.perf_counter()
# seconds=0
# def do_something():
#     print((f'sleeping {seconds} seconds'))
#     time.sleep(seconds)
#     print('done sleeping')

# threads=[]

# for _ in range(10):
#     t=threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# finish=time.perf_counter()

# for tread in threads:
#     tread.join()

# print(f'finish in {round(finish-start,2)} seconds')

# from multiprocessing import Process, Lock
# def dispmay_name(l, i):
#     l.acquire()
#     print ('Hi', i)
#     l.release()
# if __name__ == '__main__':
#     my_lock = Lock()
#     my_name = ['Aadrika', 'Adwaita', 'Sakya', 'Sanj']
# for name in my_name:
#     Process(target=dispmay_name, args=(my_lock,name)).start()

# import subprocess
# pathFFmpeg = r'/usr/bin/ffmpeg /usr/share/ffmpeg /usr/share/man/man1/ffmpeg.exe'
# pathInput = r'/home/madnan/Downloads/adnan.mp4'
# pathOutput = r'/home/madnan/Downloads/output.mp4'
# commands_list = [
#     pathFFmpeg,
#     "-i", pathInput,
#     "-c:v", "libx265",
#     "-preset", "fast",
#     "-crf", "22",
#     "-c:a", "aac",
#     "-b:a", "196k",
#     "-pix_fmt", "yuv420p", pathOutput
#     ]    
# results = subprocess.run(commands_list)
# if results.returncode==0:
#     print ("FFmpeg Script Ran Successfully")
# else:
#     print ("There was an error running your FFmpeg script")

##################### compress the video file ##################

#  def save(self, *args, **kwargs):
#         super(Videos, self).save(*args, **kwargs)
#         if self.video and not self.compressed:
#                 media_in = settings.MEDIA_ROOT+'/'+str(self.video)
#                 print(media_in)
#                 filename, extension = os.path.splitext(media_in)
#                 media_out = filename + '_temp' + extension
#                 # output_file_name = media_out.split('/media/')[-1]
#                 subprocess.run('ffmpeg -i ' + media_in + " -vcodec libx264 -crf 32 " +  media_out, shell=True)
#                 self.video = media_out
#                 self.compressed = True
#                 media_out=self.save()


###################### covert video mkv to mp4 video #################

# import os
# import ffmpeg

# start_dir = os.getcwd()
# def convert_to_mp4(mkv_file):
#     name, ext = os.path.splitext('adnan.mkv')
#     out_name = name + ".mp4"
#     ffmpeg.input(mkv_file).output(out_name).run()
#     print("Finished converting {}".format(mkv_file))

# for path, folder, files in os.walk(start_dir):
#     for file in files:
#         if file.endswith('.mkv'):
#             print("Found file: %s" % file)
#             convert_to_mp4(os.path.join(start_dir, file))
#         else:
#             pass


####################### convert video mp4 to mkv video ###############

# import os
# import ffmpeg

# start_dir = os.getcwd()
# def convert_to_mkv(mp4_file):
#     name, ext = os.path.splitext('adnan.mp4')
#     out_name = name + ".mkv"
#     ffmpeg.input(mp4_file).output(out_name).run()
#     print("Finished converting {}".format(mp4_file))

# for path, folder, files in os.walk(start_dir):
#     for file in files:
#         if file.endswith('.mp4'):
#             print("Found file: %s" % file)
#             convert_to_mkv(os.path.join(start_dir, file))
#         else:
#             pass



# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)
#     return response

        # exc_type, exc_obj, tb = sys.exc_info()
        # f = tb.tb_frame
        # lineno = tb.tb_lineno
        # filename = f.f_code.co_filename
        # linecache.checkcache(filename)
        # line = linecache.getline(filename, lineno, f.f_globals)

# import inspect
# line=inspect.currentframe().f_back.f_lineno

# filename=inspect.currentframe().f_back.f_code.co_filename
# frame = inspect.currentframe().f_back



# Facebook has detected Django Social Login isn't using a secure connection to transfer information.
# Until Django Social Login updates its security settings, you won't be able to use Facebook to log into it.