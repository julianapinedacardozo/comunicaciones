#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: ConfiguracionUSRP
# Author: Jhon Sandoval - Juliana Pineda
# Generated: Mon Feb 28 14:45:42 2022
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sys
import time
from gnuradio import qtgui


class ConfiguracionUSRP(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ConfiguracionUSRP")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ConfiguracionUSRP")
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

        self.settings = Qt.QSettings("GNU Radio", "ConfiguracionUSRP")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
        self.fc = fc = 50000000
        self.GTX = GTX = 1
        self.A = A = 1

        ##################################################
        # Blocks
        ##################################################
        self._fc_range = Range(50000000, 2200000000, 1000000, 50000000, 200)
        self._fc_win = RangeWidget(self._fc_range, self.set_fc, 'Frecuencia Portadora', "counter_slider", float)
        self.top_grid_layout.addWidget(self._fc_win)
        self._GTX_range = Range(0, 1, 0.0001, 1, 200)
        self._GTX_win = RangeWidget(self._GTX_range, self.set_GTX, 'Ganacia del TX', "counter_slider", float)
        self.top_grid_layout.addWidget(self._GTX_win)
        self._A_range = Range(0, 1, 0.0001, 1, 200)
        self._A_win = RangeWidget(self._A_range, self.set_A, 'Amplitu se\xc3\xb1al', "counter_slider", float)
        self.top_grid_layout.addWidget(self._A_win)
        self.uhd_usrp_sink_1 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_1.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_1.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_1.set_center_freq(fc, 0)
        self.uhd_usrp_sink_1.set_gain(GTX, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, A, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ConfiguracionUSRP")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_1.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.uhd_usrp_sink_1.set_center_freq(self.fc, 0)

    def get_GTX(self):
        return self.GTX

    def set_GTX(self, GTX):
        self.GTX = GTX
        self.uhd_usrp_sink_1.set_gain(self.GTX, 0)


    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A
        self.analog_sig_source_x_0.set_amplitude(self.A)


def main(top_block_cls=ConfiguracionUSRP, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
