#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ModuladorPAM_1
# Author: Jhon Sandoval - Juliana Pienda
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from ModuladorPAM import ModuladorPAM  # grc-generated hier_block
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class pulsos_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ModuladorPAM_1", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ModuladorPAM_1")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "pulsos_1")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000
        self.w = w = 50
        self.fs = fs = samp_rate/100
        self.d3 = d3 = 50
        self.d2 = d2 = 50
        self.d1 = d1 = 50

        ##################################################
        # Blocks
        ##################################################
        self._w_range = Range(0, 100, 1, 50, 200)
        self._w_win = RangeWidget(self._w_range, self.set_w, "ancho del pulso", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._w_win)
        self._d3_range = Range(0, 100, 1, 50, 200)
        self._d3_win = RangeWidget(self._d3_range, self.set_d3, "delay3", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._d3_win)
        self._d2_range = Range(0, 100, 1, 50, 200)
        self._d2_win = RangeWidget(self._d2_range, self.set_d2, "delay2", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._d2_win)
        self._d1_range = Range(0, 100, 1, 50, 200)
        self._d1_win = RangeWidget(self._d1_range, self.set_d1, "delay1", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._d1_win)
        self.qtgui_time_sink_x_3 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            4, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_3.set_update_time(0.10)
        self.qtgui_time_sink_x_3.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_3.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_3.enable_tags(True)
        self.qtgui_time_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3.enable_autoscale(False)
        self.qtgui_time_sink_x_3.enable_grid(False)
        self.qtgui_time_sink_x_3.enable_axis_labels(True)
        self.qtgui_time_sink_x_3.enable_control_panel(False)
        self.qtgui_time_sink_x_3.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_3_win = sip.wrapinstance(self.qtgui_time_sink_x_3.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_3_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            4,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, d2)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, d3)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, d1)
        self.analog_sig_source_x_0_1_2 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, 100, 1, 0, 0)
        self.analog_sig_source_x_0_1_1 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, 100, 1, 0, 0)
        self.analog_sig_source_x_0_1_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, 100, 1, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 100, 1, 0, 0)
        self.ModuladorPAM_0_2 = ModuladorPAM(
            d=w,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPAM_0_1 = ModuladorPAM(
            d=w,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPAM_0_0 = ModuladorPAM(
            d=w,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPAM_0 = ModuladorPAM(
            d=w,
            fs=fs,
            samp_rate=samp_rate,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ModuladorPAM_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.ModuladorPAM_0, 0), (self.qtgui_time_sink_x_3, 0))
        self.connect((self.ModuladorPAM_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.ModuladorPAM_0_1, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.ModuladorPAM_0_2, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.ModuladorPAM_0, 0))
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.ModuladorPAM_0_1, 0))
        self.connect((self.analog_sig_source_x_0_1_1, 0), (self.ModuladorPAM_0_2, 0))
        self.connect((self.analog_sig_source_x_0_1_2, 0), (self.ModuladorPAM_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_3, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_freq_sink_x_0, 3))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_3, 3))
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_time_sink_x_3, 2))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pulsos_1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_fs(self.samp_rate/100)
        self.ModuladorPAM_0.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_0_0.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_0_1.set_samp_rate(self.samp_rate)
        self.ModuladorPAM_0_2.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_2.set_sampling_freq(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_3.set_samp_rate(self.samp_rate)

    def get_w(self):
        return self.w

    def set_w(self, w):
        self.w = w
        self.ModuladorPAM_0.set_d(self.w)
        self.ModuladorPAM_0_0.set_d(self.w)
        self.ModuladorPAM_0_1.set_d(self.w)
        self.ModuladorPAM_0_2.set_d(self.w)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.ModuladorPAM_0.set_fs(self.fs)
        self.ModuladorPAM_0_0.set_fs(self.fs)
        self.ModuladorPAM_0_1.set_fs(self.fs)
        self.ModuladorPAM_0_2.set_fs(self.fs)

    def get_d3(self):
        return self.d3

    def set_d3(self, d3):
        self.d3 = d3
        self.blocks_delay_0_0.set_dly(self.d3)

    def get_d2(self):
        return self.d2

    def set_d2(self, d2):
        self.d2 = d2
        self.blocks_delay_0_1.set_dly(self.d2)

    def get_d1(self):
        return self.d1

    def set_d1(self, d1):
        self.d1 = d1
        self.blocks_delay_0.set_dly(self.d1)




def main(top_block_cls=pulsos_1, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
