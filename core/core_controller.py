from handler.handler_ui import HandlerUI
# from handler.handler_plot import HandlerPlot
# from handler.handler_log import HandlerLog
# from handler.handler_comm_gse import HandlerCommGSE
# from handler.handler_comm_umb import HandlerCommUMB
# from handler.handler_comm_tlm import HandlerCommTLM

class CoreController:
    def __init__(self):
        # UI 초기화
        self.ui = HandlerUI()

        # 핸들러 초기화
        # self.plot_handler = HandlerPlot(self.ui)
        # self.log_handler = HandlerLog()
        # self.gse_handler = HandlerCommGSE(self)
        # self.umb_handler = HandlerCommUMB(self)
        # self.tlm_handler = HandlerCommTLM(self)

        # UI에 핸들러 연결
        self.ui.set_controller(self)

    def start(self):
        self.ui.show()
