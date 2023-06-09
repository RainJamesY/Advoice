import argparse
import os

import soundfile as sf
import torch

from data_utils import denormalize, file2mel, load_model, mel2wav, normalize


def main(model_dir: str, source: str, target: str, output: str):
    model, config, attr, device = load_model(model_dir)

    path = target
    rePath = "D:/Storage/Pycharm Project/attack-vc-master"

    file_list = os.listdir(path)
    src_mel = file2mel(source, **config["preprocess"])
    src_mel = normalize(src_mel, attr)
    src_mel = torch.from_numpy(src_mel).T.unsqueeze(0).to(device)


    for file_name in file_list:

        file_path = os.path.join(path, file_name)

        result_path = os.path.join(rePath, file_name)
        target = file_path

        tgt_mel = file2mel(target, **config["preprocess"])
        tgt_mel = normalize(tgt_mel, attr)
        tgt_mel = torch.from_numpy(tgt_mel).T.unsqueeze(0).to(device)

        with torch.no_grad():
            out_mel = model.inference(src_mel, tgt_mel)
            out_mel = out_mel.squeeze(0).T
        out_mel = denormalize(out_mel.data.cpu().numpy(), attr)
        out_wav = mel2wav(out_mel, **config["preprocess"])

        sf.write(result_path, out_wav, config["preprocess"]["sample_rate"])

    # src_mel = file2mel(source, **config["preprocess"])
    # tgt_mel = file2mel(target, **config["preprocess"])
    #
    # src_mel = normalize(src_mel, attr)
    # tgt_mel = normalize(tgt_mel, attr)
    #
    # src_mel = torch.from_numpy(src_mel).T.unsqueeze(0).to(device)
    # tgt_mel = torch.from_numpy(tgt_mel).T.unsqueeze(0).to(device)
    #
    # with torch.no_grad():
    #     out_mel = model.inference(src_mel, tgt_mel)
    #     out_mel = out_mel.squeeze(0).T
    # out_mel = denormalize(out_mel.data.cpu().numpy(), attr)
    # out_wav = mel2wav(out_mel, **config["preprocess"])
    #
    # sf.write(output, out_wav, config["preprocess"]["sample_rate"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_dir", type=str, default="D:\\Storage\\Pycharm Project\\attack-vc-master\\vctk_model", help="The directory of model files.")
    parser.add_argument(
        "--source", type=str, default="D:\\Storage\\Pycharm Project\\attack-vc-master\\Self.wav", help="The source utterance providing linguistic content."
    )
    parser.add_argument(
        "--target", type=str,default="D:\\Storage\\Pycharm Project\\attack-vc-master\\3people\\te", help="The target utterance providing vocal timbre."
    )
    parser.add_argument("--output", type=str, default="D:\\Storage\\Pycharm Project\\attack-vc-master\\",help="The output converted utterance.")
    main(**vars(parser.parse_args()))
