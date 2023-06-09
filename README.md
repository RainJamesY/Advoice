# 防御语音合成：基于对抗样本的主动防御手段

内容安全课程项目源码

组长：陈品极

组员：姚栋宇 张培妍 万宇宁

### 环境配置

* Windows 10 + Anaconda + python3

### 数据集

* 采用数据集来源于CSTR VCTK Corpu，完整数据集可在此处下载[here](https://datashare.ed.ac.uk/handle/10283/3443)，目录/3people下为部分测试数据集。

* ```
  Defended
  └─ 3people
     ├─ p333
     └─ p374
  ```

### 目录介绍

在这里我们介绍我们的目录结构，以便您进行测试。

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

### 测试

如果您想自己运行代码测试生成的防御语音效果，请运行 ./Web_attack.py 文件，并修改以下几点：

* output : 将其修改为您想保存结果文件的路径几名称，如：./result/output.wav，结果文件将存储至您当前目录下的 result 文件夹中，并命名为 output.wav
* eps : 扰动大小，您可以尝试 0-1 以内的任何值来测试效果
* n_iters : 迭代次数，您可以修改为任意值来测试效果，我们建议您使用1500
* examples : 您可以修改其中音频路径，这将作为在 gradio 网页端时的测试用例，修改手册可见[here](https://www.gradio.app/guides)

如果您只想测试防御效果，请登录我们的网站进行防御测试：

* 在以下网站进行[防御语音生成](https://huggingface.co/spaces/petervavank/Advoice)：点击examples提供的语音样本进行测试，生成即为防御语音样本。（您也可以选用自己的语音样本进行测试）
* 在以下网站进行[语音转换](https://huggingface.co/spaces/petervavank/VoiceConvertion)测试效果：点击examples提供的语音样本进行测试，其中提供音色的样本分别为防御前后的语音样本，对比语音转换结果，可以看到我们的防御效果（您也可以选用自己的语音样本进行测试）

测试中出现任何问题，请联系peiyan_zhang@qq.com