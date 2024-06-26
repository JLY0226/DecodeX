Copyright (C) [2024] BEIJING INSTITUTE OF OPEN SOURCE CHIP(BOSC)
DECODEX is licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed 
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR 
CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

# Introduction to DecodeX
* DecodeX is a mini decoding tool designed for the RISC-V architecture, which can decode 32-bit instruction code into readable disassembly instructions for developers to debug. The RV64GBKVC extended instruction set is currently supported. In addition, the tool integrates spike decoding tools, decoding information will contain spike simulator decoding results, users can double check.
* DecodeX是一款专为RISC-V架构设计的mini解码工具，它能够将32位指令码解码成可读的反汇编指令，方便开发者进行调试。目前支持RV64GBKVC扩展指令集。此外，该工具集成了spike的解码工具，解码信息会包含spike模拟器的解码结果，可供用户double check。

DecodeX provides support for the following aspects of the RISC-V ISA:
* RV64G (IMAFDCZicsr_Zifencei)
* RV32G
* V extension 1.0


# DecodeX Quick Start Guide for RISC-V
- Clone this repo: `git@github.com:JLY0226/DecodeX.git`
- Set the following environment variables. 
    - `export DECODEX=(Installation/path/for/DecodeX) /DecodeX`
    - `alias dec='python3 $DECODEX/dec.py'`
- Execute the command at the command line to enter the interactive interface: `dec`
- Enter the command code:(eg) `02e70bb3`
- Get the decoding result: 
    - `inst:2e70bb3`
    - `asm: MUL x23,x14,x14`
    - `decode_info: name = MUL,type = R, rd = x23(s7), rs1 = x14(a4), rs2 = x14(a4)`
    - `spike_asm:  mul s7, a4, a4`