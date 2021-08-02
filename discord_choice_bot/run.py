# coding:utf-8

import os
import random
from textwrap import dedent
from typing import List

import discord
from discord.client import Client


class bot:

    client: Client = discord.Client()

    def run(self, token) -> None:
        bot.client.run(token)

    def help(self) -> str:
        output: str = """
        >>> ランダムにチョイスしちゃうよ！
        こんな風に使ってね〜

        Example：
        `!chobo 9`
        `!chobo 59`
        `!chobo りんご ばなな ぶどう みかん`
        """
        return dedent(output)[1:-1]

    def choice(self, text: str) -> str:
        def choice_dice(query: List[str]) -> str:
            output: str = ""
            try:
                result: int = random.randint(1, int(query[0]))
                output += f"""
                **{result}**が選ばれたよ〜
                """
            except Exception as e:
                print(f"choice_dice Error: {e}")
                output += f"""
                「{query[0]}」ってなに？僕にはわからないよぉ
                """
            print(f"choice_dice: {output.strip()}")
            return output

        def choice_char(query: List[str]) -> str:
            result: str = random.sample(query, k=1)[0]
            output: str = f"""
            **{result}**が選ばれたよ〜
            """
            print(f"choice_char: {output.strip()}")
            return output

        query: List[str] = text.split()[1:]
        output: str = ""
        if len(query) == 0:
            output += """
            **!chobo**のあとに数字か文字列を入力してね〜
            詳しくは、**!chobo-help**
            """
        elif len(query) == 1:
            output += choice_dice(query)
        else:
            output += choice_char(query)

        return dedent(output)[1:-1]
        # return output

    @staticmethod
    @client.event
    async def on_ready():
        print("ログインしました")

    @staticmethod
    @client.event
    async def on_message(message):
        if message.author.bot:
            return

        if "!chobo-help" in message.content:
            await message.channel.send(bot.help(bot))

        elif "!chobo" in message.content:
            await message.channel.send(bot.choice(bot, message.content))

        elif "/neko" in message.content:
            output: str = "この機能はお楽しみ終了となりますた"
            await message.channel.send(bot.choice(bot, output))


if __name__ == "__main__":
    TOKEN: str = os.environ["DISCORD_BOT_TOKEN"]
    bot().run(TOKEN)
