
import silentcipher

# cuda or cpu
device = 'cpu'

model = silentcipher.get_model(
    ckpt_path='Models/44_1_khz/73999_iteration',
    config_path='Models/44_1_khz/73999_iteration/hparams.yaml',
    model_type='44.1k',
    device=device
)



def main():
    
    filename='sample/wav/audio_mono_44k.wav'
    encoded_filename='sample/enc/audio_mono_44k_enc.wav'
    
        # Encode from filename
    model.encode(filename, encoded_filename, [123, 234, 111, 222, 11], message_sdr=None)
    




if __name__=="__main__":
    main()