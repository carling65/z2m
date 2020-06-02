z2m (Zoom G3 to midi foot controller)

z2mはZoom G3またはZoom G3Xを、仮想midiケーブルを介することで、任意のDAWで
midiフットコントローラとして使用することを可能にするソフトウェアです。

# 必要なもの
Zoom G3(ver2.10) または Zoom G3X(ver2.10)
loopMIDI(http://www.tobias-erichsen.de/software/loopmidi.html)

# 使用方法
1. Zoom G3上で、すべてのエフェクトを「T Scream」に設定したパッチを用意する。
2. Zoom G3とPCをUSBケーブルで接続する。
3. loopMIDIを起動し、Nameが「loopMIDI Port」である仮想MIDIケーブルが有ることを確認する。なければ作成する。
4. Zoom G3のすべてのエフェクトのスイッチがオフになっていることを確認する。
5. z2m.exeを実行する。
6. ペダルを踏むとloopMIDIにmidiメッセージが送られる。
7. 各自所有するDAWやエフェクトソフトウェアの設定をする。

# 動作説明
ペダルを踏むとその位置に対応したMIDIメッセージが仮想MIDIポートに対して送られる。
初期設定では左側から順に B0 00,B0 01,B0 02,B0 03,B0 04,B0 05 が送られる。
この内B0の部分に関しては、config.ini内のSTATUS_BYTEの値を変更することによって変更可能。
ペダルのオンオフに関わらず、スイッチを踏むと同じ信号が送信される。

所有するデバイスがZoom G3Xの場合は、START_SYSEXを
 [0x52,0x00,0x59,0x50]
と変更してください。
またMIDI OUTに任意の名前のポートやデバイスを使う場合も、
それに合致するように OUTPUT_DEVICE_NAME の値を変更してください。

# コンタクト
意見、要望、不具合等がある場合は以下より。
http://blog.livedoor.jp/carling_65/

# 参考にしたサイト 使用したライブラリ
1.
ZOOM G3X(v2.10)をMIDIコントローラーとして使う - おぼえがき
https://tpcbtw.hatenablog.com/entry/2018/06/09/173129

2.
GitHub - gesellkammer/rtmidi2: python bindings to rtmidi allowing to listen to multiple ports simultaneously
https://github.com/gesellkammer/rtmidi2

3.
PythonでMIDIフェーダと通信するメモ（MIDIデバイス→PC) - Qiita
https://qiita.com/Dr10_TakeHiro/items/e6df6c9b59869a74f899


------------------------------------------------


z2m (Zoom G3 to midi foot controller)

The z2m allows the Zoom G3 or Zoom G3X to be used with any DAW and software FX over a virtual midi cable.
This Software allows you to use it as a MIDI foot controller.

# What you need.
Zoom G3(ver2.10) or Zoom G3X(ver2.10)
loopMIDI(http://www.tobias-erichsen.de/software/loopmidi.html)

# Usage
1. prepare a patch with all effects set to "T Scream" on Zoom G3.
2. Connect the Zoom G3 to your PC with a USB cable.
3. Start loopMIDI and confirm that you have a Virtual MIDI Cable whose Name is "loopMIDI Port". If not, create one.
4. Make sure that all effects on the Zoom G3 are switched off.
5. run z2m.exe.
6. When you step on the pedal, a midi message is sent to loopMIDI.
7. Set up your own DAW and effect software.

# Description
When you step on a pedal, a MIDI message corresponding to the position is sent to the virtual MIDI port.
By default, B0 00, B0 01, B0 02, B0 03, B0 04, B0 05 are sent from the left side in order.
The B0 part can be changed by changing the value of STATUS_BYTE in config.ini.
Regardless of whether the pedal is on or off, the same signal is sent when the switch is pressed.

If the device you own is a Zoom G3X, set START_SYSEX to
 [0x52,0x00,0x59,0x50]
You can also use a port or device of any name for MIDI OUT.
Change the value of OUTPUT_DEVICE_NAME to match the value of it.

# Contact.
If you have any opinions, requests, or defects, please contact us below.
http://blog.livedoor.jp/carling_65/

# Reference
1.
ZOOM G3X(v2.10)をMIDIコントローラーとして使う - おぼえがき
https://tpcbtw.hatenablog.com/entry/2018/06/09/173129

2.
GitHub - gesellkammer/rtmidi2: python bindings to rtmidi allowing to listen to multiple ports simultaneously
https://github.com/gesellkammer/rtmidi2

3.
PythonでMIDIフェーダと通信するメモ（MIDIデバイス→PC) - Qiita
https://qiita.com/Dr10_TakeHiro/items/e6df6c9b59869a74f899
