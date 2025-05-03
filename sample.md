
# input Video
Place video.mp4

# h264 Video

## h264_nvenc

```sh
ffmpeg -i "input/video.mp4" \
-vf "scale=576:1024" -c:v h264_nvenc -b:v 1500k -an "h264_nvenc/video_576x1024_1500k.mp4" \
-vf "scale=480:854" -c:v h264_nvenc -b:v 1000k -an "h264_nvenc/video_480x854_1000k.mp4" \
-vf "scale=360:640" -c:v h264_nvenc -b:v 750k -an "h264_nvenc/video_360x640_750k.mp4"
```

## libx264

### 576x1024 @ 1500k
```sh
ffmpeg -i "input/video.mp4" -vf "scale=576:1024" -c:v libx264 -b:v 1500k -an "libx264/video_576x1024_1500k.mp4"
```

### 480x854 @ 1000k
```sh
ffmpeg -i "input/video.mp4" -vf "scale=480:854" -c:v libx264 -b:v 1000k -an "libx264/video_480x854_1000k.mp4"
```

### 360x640 @ 750k
```sh
ffmpeg -i "input/video.mp4" -vf "scale=360:640" -c:v libx264 -b:v 750k -an "libx264/video_360x640_750k.mp4"
```

# aac Audio

```sh
ffmpeg -i "input/video.mp4" -vn -c:a aac -b:a 128k -ac 2 -ar 44100 "aac/audio_st.mp4"
```


```sh
ffmpeg -i "input/video.mp4" -vn -c:a aac -b:a 128k -ac 1 -ar 44100 "aac/audio_mono.mp4"
```


# wav audio

## 16bit audio

```sh
ffmpeg -i "input/video.mp4" -vn -c:a pcm_s16le -ac 1 -ar 44100 "wav/audio_mono_44k.wav"
```

## 32bit audio

```sh
ffmpeg -i "input/video.mp4" -vn -c:a pcm_s32le -ac 2 -ar 44100 "wav/audio_32bit_st_44k.wav"
```

```sh
ffmpeg -i "input/video.mp4" -vn -c:a pcm_s32le -ac 1 -ar 44100 "wav/audio_32bit_mono_44k.wav"
```

