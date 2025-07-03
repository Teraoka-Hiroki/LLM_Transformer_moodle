# step01_hello_ai.py

import torch

def check_environment():
    """
    PyTorchのバージョンとGPUの認識状態を確認して表示する関数
    """
    print("Hello, AI World! これからTransformerを作る冒険を始めよう！")

    # PyTorchのバージョンを表示
    print(f"PyTorchのバージョン: {torch.__version__}")

    # GPUが利用可能かを確認
    if torch.cuda.is_available():
        # 利用可能なGPUの数を取得
        gpu_count = torch.cuda.device_count()
        # 0番目のGPUの名前を取得
        gpu_name = torch.cuda.get_device_name(0)
        print(f"GPUは正しく認識されています: {gpu_name} ({gpu_count}個のGPUが利用可能です)")
    else:
        print("GPUは認識されていません。CPUで実行します。")

if __name__ == "__main__":
    check_environment()