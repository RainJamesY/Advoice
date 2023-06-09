import argparse
import os
import gradio as gr
import numpy as np
import soundfile as sf
import torch

from attack_utils import emb_attack
from data_utils import denormalize, file2mel, load_model, mel2wav, normalize


def main(
        vc_tgt: str,
        adv_tgt: str,
):
    model_dir = "./vctk_model"
    output = "./result/output.wav"
    eps = 0.5
    n_iters = 1500
    attack_type = "emb"

    assert attack_type == "emb"
    model, config, attr, device = load_model(model_dir)

    vc_tgt = file2mel(vc_tgt, **config["preprocess"])
    adv_tgt = file2mel(adv_tgt, **config["preprocess"])

    vc_tgt = normalize(vc_tgt, attr)
    adv_tgt = normalize(adv_tgt, attr)

    vc_tgt = torch.from_numpy(vc_tgt).T.unsqueeze(0).to(device)
    adv_tgt = torch.from_numpy(adv_tgt).T.unsqueeze(0).to(device)

    adv_inp = emb_attack(model, vc_tgt, adv_tgt, eps, n_iters)

    adv_inp = adv_inp.squeeze(0).T
    adv_inp = denormalize(adv_inp.data.cpu().numpy(), attr)
    adv_inp = mel2wav(adv_inp, **config["preprocess"])

    sf.write(output, adv_inp, config["preprocess"]["sample_rate"])

    return output


inputs = [
    gr.inputs.Audio(type="filepath", label="Audio1"),
    gr.inputs.Audio(type="filepath", label="Audio2"),
]

examples = [
    ["./3people/p333/p333_003.wav",
     "./3people/p374/p374_003.wav"]
]
demo = gr.Interface(fn=main,
                    inputs=inputs,
                    examples=examples,
                    outputs=gr.Audio(type="filepath", label="Output")
                    )

if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    # main()
    demo.launch()
