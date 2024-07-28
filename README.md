# Advoice: Proactively Defend against AI-synthesized Fake Voices via Adversarial Attacks

Content Security Course Project Source Code

**Team Leader**: Chen Pinji

**Team Members**: Yao Dongyu, Zhang Peiyan, Wan Yuning

### Environment Setup

* Windows 10 + Anaconda + Python 3

### Dataset

* The dataset is sourced from the CSTR VCTK Corpus. The complete dataset can be downloaded [here](https://datashare.ed.ac.uk/handle/10283/3443). A subset for testing is available in the `/3people` directory.

* ```
  Defended
  └─ 3people
     ├─ p333
     └─ p374
  ```

### Directory Overview

Below is an overview of our directory structure to facilitate testing.

```
Defended
├─ vctk_model
│  ├─ model.ckpt
│  ├─ config.yaml
│  └─ attr.pkl
└─ 3people
│  ├─ p333
│  └─ p374
└─ result
└─ Web_attack.py
└─ models.py
└─ inference.py
└─ generate_masking_threshold.py
└─ data_utils.py
└─ attack_utils.py
```

### Testing

To run code tests for generating defended voice samples, execute the `./Web_attack.py` file and adjust the following parameters:

* **output**: Modify this to the path and name where you want to save the result file, e.g., `./result/output.wav`. The result file will be stored in the `result` folder under your current directory and named `output.wav`.
* **eps**: Perturbation size; you can test any value between 0-1 for different effects.
* **n_iters**: Number of iterations; you can set this to any value for testing purposes. We recommend using 1500.
* **examples**: You can modify the audio paths here for testing on the Gradio web interface. The modification guide can be found [here](https://www.gradio.app/guides).

If you only want to test the defense effect, please visit our website for defense testing:

* Generate defended voice samples on this [Defense Voice Generation](https://huggingface.co/spaces/petervavank/Advoice) page: Click on the provided voice samples in examples to test, and the generated sample will be the defended voice sample (you can also use your own voice samples for testing).
* Test the effect of voice conversion on this [Voice Conversion](https://huggingface.co/spaces/petervavank/VoiceConvertion) page: Click on the provided voice samples in examples to test. The provided samples include voice samples before and after the defense. Compare the voice conversion results to observe the defense effect (you can also use your own voice samples for testing).

If you encounter any issues during testing, please contact peiyan_zhang@qq.com.
