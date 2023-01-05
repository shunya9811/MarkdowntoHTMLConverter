import markdown
import sys

def main():
    argLen = len(sys.argv)
    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    # 入力ファイル、出力ファイルの拡張子がそれぞれ.md .htmlじゃない場合が考えられる

    if argLen == 4 and command == "markdown": 
        try:
            with open(input_file, "r") as f:
                md = f.read()

            html = markdown.markdown(md)

            with open(output_file, "w") as f:
                f.write(html)

        except FileNotFoundError:
            print("入力ファイルが存在しません")
    else:
        print("入力が正しくありません")
        sys.exit()


if __name__ == "__main__":
    main()
