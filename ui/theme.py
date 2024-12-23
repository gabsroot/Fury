import dearpygui.dearpygui as dpg

class Theme:
    @staticmethod
    def window():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # background color
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (0, 18, 33, 255))
                # border color
                dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 18, 33, 255))
                # text color
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                # topbar color
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (13, 26, 41, 255))
                # close button hover color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (18, 56, 82, 255))
                # close button active color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (18, 56, 82, 255))
                # tab default color
                dpg.add_theme_color(dpg.mvThemeCol_Tab, (12, 26, 38, 255))
                # tab hover color
                dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (18, 56, 82, 255))
                # tab active color
                dpg.add_theme_color(dpg.mvThemeCol_TabActive, (18, 56, 82, 255))
                
        return theme
    
    @staticmethod
    def button():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # text color
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                # default color
                dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 41, 71, 255))
                # hover color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (59, 68, 88, 255))
                # active color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (72, 81, 102, 255))
                # border radius
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)

        return theme
    
    @staticmethod
    def checkbox():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # text color
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                # bg default color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (36, 38, 51, 255))
                # hover color
                dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, (36, 38, 51, 255))
                # active color
                dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, (36, 38, 51, 255))
                # mark color
                dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (38, 203, 190, 255))
                # border radius
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)

        return theme
    
    @staticmethod
    def combo():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # text color
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                # text indent
                dpg.add_theme_style(dpg.mvPlotStyleVar_AnnotationPadding, 0.05)
                # bg default color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (36, 38, 51, 255))
                # bg hover color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (36, 38, 51, 255))
                # border radius
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
                # popup default color
                dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (36, 38, 51, 255))
                # popup border radius
                dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 4)
                # item hover color
                dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (59, 68, 88, 255))
                # item active color
                dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (72, 81, 102, 255))
                # item selected color
                dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, (36, 38, 51, 255))
                # padding
                dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 30, 10)
                # button default color
                dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 41, 71, 255))
                # button hover color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (59, 68, 88, 255))
                # button active color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (72, 81, 102, 255))
                # tab scroll default color
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (0, 18, 33, 255))
                # scroll bar default color
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (18, 31, 46, 255))
                # scroll bar hover color
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (18, 31, 46, 255))
                # scroll bar active color
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (18, 31, 46, 255))

        return theme
    
    @staticmethod
    def input():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # text color
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                # bg default color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (36, 38, 51, 255))
                # border radius
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
                # color selector
                dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, (59, 68, 88, 255))
                
        return theme
    
    @staticmethod
    def slider():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # text color
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                # default color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (36, 38, 51, 255))
                # hover color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (36, 38, 51, 255))
                # active color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (36, 38, 51, 255))
                # border radius
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
                # circle default color
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (87, 87, 87, 255))
                # circle active color
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (87, 87, 87, 150))
                # round cicle
                dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 3)
                # width circle
                dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize, 10)
                # padding circle
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 3)

        return theme
    
    @staticmethod
    def color_picker():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # btn border radius
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
                # popup border radius
                dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 8)
                # popup bg color
                dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (13, 26, 41, 255))
                # popup border color
                dpg.add_theme_color(dpg.mvPlotCol_FrameBg, (18, 56, 82, 255))
                # btn 
                dpg.add_theme_color(dpg.mvPlotCol_PlotBorder, (0, 41, 71, 255))
                # btn hover
                dpg.add_theme_color(dpg.mvPlotCol_LegendBg, (59, 68, 88, 255))
                # btn click
                dpg.add_theme_color(dpg.mvPlotCol_LegendBorder, (59, 68, 88, 255))
                # color selector
                dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, (59, 68, 88, 255))
                # padding
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 2)
                
        return theme
