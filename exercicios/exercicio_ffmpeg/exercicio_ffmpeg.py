# https://ffmpeg.org/documentation.html

"""
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k -c:s srt -map v:0 -map a
-map 1:0 -ss 00:00:00 -to 00:00:50 "SAIDA"
"""

import os, fnmatch, sys

if sys.platform == 'linux':
    command_ffmpeg = 'ffmpeg'
else:
    command_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:50'
extent_output = '.mkv'

path_origin = r'E:\temp\mp4'
path_destination = r'E:\temp\mkv'

for root, dirs, files in os.walk(path_origin):
    for file in files:
        if not fnmatch.fnmatch(file, '*.mp4'):
            continue
        full_path = os.path.join(root, file)
        file_name, file_extent = os.path.splitext(full_path)
        path_subtitle = file_name + '.srt'

        if os.path.isfile(path_subtitle):
            input_subtitle = f'-i "{path_subtitle}"'
            map_subtitle = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_subtitle = ''
            map_subtitle = ''

        file_name, file_extent = os.path.splitext(file)

        output_path = fr'{path_destination}\{file_name}_NOVO{extent_output}'

        command_full = f'{command_ffmpeg} -i "{full_path}" {input_subtitle} ' \
                       f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
                       f'{debug} {map_subtitle} "{output_path}"'

        os.system(command_full)
