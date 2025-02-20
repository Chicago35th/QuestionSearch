import os
import pandas as pd
from pypinyin import pinyin, Style
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.text import LabelBase

# 注册中文字体（需在GitHub仓库添加字体文件）
LabelBase.register('msyh', 'msyh.ttf')


class SearchApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # 搜索输入框
        self.search_input = TextInput(
            hint_text='输入拼音首字母搜索...',
            font_name='msyh',
            size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.search_input)

        # 结果显示
        self.result_label = Label(
            text='准备就绪',
            font_name='msyh',
            size_hint=(1, 0.9)
        )
        self.layout.add_widget(self.result_label)

        # 绑定实时搜索
        self.search_input.bind(text=self.on_text_change)
        self.df = self.load_data()
        return self.layout

    def load_data(self):
        """智能路径处理"""
        try:
            # 自动识别Android环境
            if 'ANDROID_ARGUMENT' in os.environ:
                from android.storage import app_storage_path
                path = os.path.join(app_storage_path(), 'data.csv')
            else:
                path = os.path.join(os.path.dirname(__file__), 'data.csv')

            df = pd.read_csv(path)
            df['首字母'] = df['题干'].apply(self.get_pinyin)
            return df
        except Exception as e:
            return pd.DataFrame()

    def get_pinyin(self, text):
        return ''.join([p[0][0].upper() for char in str(text)
                        for p in pinyin(char, style=Style.FIRST_LETTER)])

    def on_text_change(self, instance, value):
        """实时搜索"""
        query = value.upper()
        if not self.df.empty and query:
            results = self.df[self.df['首字母'].str.contains(query)]
            self.show_results(results)

    def show_results(self, df):
        text = "\n".join([
            f"{row['题型']} | {row['题干'][:20]}... | 答案：{row['答案']}"
            for _, row in df.iterrows()
        ]) or "无匹配结果"
        self.result_label.text = text


if __name__ == '__main__':
    SearchApp().run()