import ctypes
import argparse
import os
import subprocess

decodex = os.environ.get('DECODEX')
so_dir = decodex + "/decode.so"
mylib = ctypes.CDLL(so_dir)
spike_dasm_path = decodex +"/spike-dasm"

class CfCtrl_t(ctypes.Structure):
    _fields_ = [
        ("inst", ctypes.c_uint32)
    ]

cfctrl = CfCtrl_t()

def to_uint32(value):
    return ctypes.c_uint32(int(value, 16)).value

def spike_dec(inst,spike_dasm_path):
    cmd = f'echo "DASM({inst})" | {spike_dasm_path}'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print("spike_asm: ", result.stdout)

def print_info():
    print("****************************************")
    print("*    RISC-V Instruction Decode Tool    *")
    print("*         ToolName: DecodeX            *")
    print("*         Author: jiangliyang          *")
    print("*         Version: 1.2                 *")
    print("*         Date: 2024-6-24              *")
    print("****************************************")
    print("\n")

def main():
    print_info()
    while True:
        inst = input("Enter instruction (or 'q' to quit): ")
        if inst.lower() == 'q':
            break
        inst_u32 = to_uint32(inst)
        mylib.decode_inst(inst_u32)
        spike_dec(inst,spike_dasm_path)
        print("\n")
    
if __name__ == "__main__":
  main()

