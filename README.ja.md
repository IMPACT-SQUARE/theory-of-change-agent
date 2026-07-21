# Theory of Change Agent

[English](README.md) · [한국어](README.ko.md) · **日本語** · [Tiếng Việt](README.vi.md)

事業の狙いや活動は整理できていても、それを PDM の文章や指標に落とし込む作業は簡単ではありません。
Theory of Change Agent は、対話を通じてその整理を進めるためのツールです。

質問に一つずつ答えると、社会課題、活動、アウトプット、アウトカム、インパクトをつなぐ結果連鎖を
組み立てます。国際開発協力では **PDM** を、インパクトスタートアップ、
CSR、非営利では **セオリー・オブ・チェンジ図** を作成します。Claude などの AI 環境で使え、
会話した言語で応答します。

## こんなときに使います

- 国際開発協力プロジェクトの PDM を初めて作成するとき
- 提出前にドラフトをガイドラインに照らして確認するとき
- 事業アイデアをインパクトの筋道として整理するとき

## はじめ方

1. 下記の手順でスキルをインストールします。
2. チャットで *「Theory of Change Agent で PDM を作って」* と入力します。事業計画書や年次報告書を添付しても構いません。
3. 質問に答え、内容が固まったら **「確定」** と伝えます。
4. `out/` を開きます。国際開発協力では `pdm.md`、それ以外では `toc.md` が主な成果物です。

## インストール

**必要なもの:** Claude Code、Claude デスクトップ、または claude.ai と `python3` です。デスクトップと Web のコード実行環境には Python が含まれます。

### いちばん簡単な方法: AI エージェントに貼り付ける (Claude Code · Antigravity など)

Claude Code、Antigravity、Gemini CLI のようにローカルでコマンドを実行できる AI エージェントを開き、以下の段落をそのまま貼り付けてください。あとはエージェントが実行します。

> Theory of Change Agent をインストール: `git clone --single-branch --depth 1 https://github.com/IMPACT-SQUARE/theory-of-change-agent.git ~/theory-of-change-agent` を実行し、その中の `skills/theory-of-change-agent` フォルダをあなたの環境のグローバルスキルフォルダにシンボリックリンク（またはコピー）して — Claude Code → `~/.claude/skills/`, Antigravity → `~/.gemini/config/skills/`, Gemini CLI → `~/.gemini/skills/`。スキルフォルダに `SKILL.md` があることを確認してから、「Theory of Change Agent で PDM を作って」と言えば開始できること（Antigravity はセッション再起動後）、更新は `git -C ~/theory-of-change-agent pull` で行えることを教えて。

*(Claude ウェブ/デスクトップの通常チャットはローカルファイルにアクセスできないため、この方法は使えません — その場合は下のプラグイン/zip の方法を使ってください。)*

### Claude Code

```
/plugin marketplace add IMPACT-SQUARE/theory-of-change-agent
/plugin install theory-of-change-agent@impact-square
```

更新は `/plugin update theory-of-change-agent` を実行します。

### Claude デスクトップ (プラグイン)

1. `Settings → Plugins → Add → Add marketplace → **Add from a repository**`
2. URL 欄に `https://github.com/IMPACT-SQUARE/theory-of-change-agent` を貼り付けてマーケットプレイスを追加します。
3. 一覧から **theory-of-change-agent** をインストールし、チャットに「Theory of Change Agent で PDM を作って」と入力します。

> 更新は自動ではありません — `Settings → Plugins` でマーケットプレイスの **Update** ボタンを押してください。

### zip アップロード (Antigravity · claude.ai など)

1. スキルを zip 化するか、同梱の `theory-of-change-agent.zip` を使います。
   ```bash
   cd skills && zip -r theory-of-change-agent.zip theory-of-change-agent \
     -x '*/.DS_Store' -x '*/out/*' -x '*/.omc/*' -x '*/__pycache__/*'
   ```
2. Claude デスクトップの `Settings → Skills → Add → Upload`、Antigravity の Skills 画面、または claude.ai の `Settings → Capabilities → Skills → Upload` からアップロードします。コード実行が使える有料プランが必要です。
3. チャットで *「Theory of Change Agent で PDM を作って」* と入力します。

> アプリへアップロードしたスキルは自動更新されません。変更後は zip をアップロードし直してください。
> Antigravity で Mermaid 図がコードとして表示される場合は Open VSX から `bierner.markdown-mermaid` を入れるか、
> 同時に出力されるテキスト版を確認してください。詳しくは [INSTALL-desktop.md](./skills/theory-of-change-agent/INSTALL-desktop.md) を参照してください。

### Git

```bash
git clone git@github.com:IMPACT-SQUARE/theory-of-change-agent.git
ln -s "$(pwd)/theory-of-change-agent/skills/theory-of-change-agent" ~/.claude/skills/theory-of-change-agent
```

## 用途と成果物

| 用途 | 成果物 | 最初に用意するもの |
|---|---|---|
| 国際開発協力プロジェクト | PDM | アイデア、提案書、既存 PDM |
| インパクトスタートアップ・新規事業 | セオリー・オブ・チェンジ図 | 事業計画書、または解決したい課題 |
| CSR・ESG プロジェクト | セオリー・オブ・チェンジ図 | 事業概要書、または提案書 |
| 非営利プログラム | セオリー・オブ・チェンジ図 | 年次報告書、またはプログラム資料 |

新しい PDM は確定前に構造チェックを受けます。承認済みの PDM は監査モードで確認でき、
文書を変更せずにガイドラインとの相違だけを報告します。

## 会話の例

```
あなた:  Theory of Change Agent で PDM を作って。
Agent:    どのような事業ですか？
          ① 国際開発協力（PDM） ② インパクトスタートアップ
          ③ CSR・ESG             ④ 非営利
あなた:  ① ラオスの母子保健事業です。
Agent:    この事業が解決したい問題は何ですか。誰がどのような困難を抱えていますか？
あなた:  農村部の妊産婦が自宅で出産しています。保健施設は遠く、信頼も十分ではありません。
Agent:    問題は高い自宅分娩率で、施設へのアクセスと信頼の不足が背景にありそうです。
          アウトカムは「保健施設で出産する女性が増える」と書けます。
          「研修回数を増やす」は活動またはアウトプットです。この方向で進めますか？
          …
あなた:  確定
Agent:    ✔ 重要ルール 8 件を通過しました。
          ⚠ アウトカム 2 の「教育の拡大」は回数を表しています。行動の変化が分かる表現に直しましょう。
          結果: out/pdm.md
```

## 仕組み

**対話 → 結果連鎖の構築 → 内容確認 → 検証 → 出力** の順で進みます。

まず、構造的で、多くの人に実際の不利益をもたらす社会課題を定義します。次に現象と原因を分け、
原因に働きかける状態の変化をアウトカムとして整理します。活動の拡大や漠然とした便益は、
アウトカムとは区別します。

年次報告書のように複数のプロジェクトが含まれる資料では、組織全体を整理するか、対象を一つの
プロジェクトに絞るかを最初に選べます。

| ファイル | 内容 |
|---|---|
| `pdm.md` | 4×4 PDM マトリックス |
| `toc.md` | Mermaid 非対応の閲覧環境でも読めるテキスト版を含むセオリー・オブ・チェンジ図 |
| `details/monitoring.md` | 指標定義、計算式、ベースライン、目標、情報源、収集時期と担当をまとめた測定計画 |
| `budget.md` | 活動別の費目、計算根拠、資金分担、年次合計をまとめた予算書。任意 |
| `details/toc.json` | 各成果物の元になるデータ |

会話、PDF、韓国語 HWP ファイル（`.hwp`、`.hwpx`）から始められます。HWP 抽出器は外部依存がなく、
アプリのコード実行環境でも動作します。

## 確認できる検証

- **決定論的品質ゲート:** 純粋な Python で重要な構造ルール 8 件を検査します。インパクト指標の禁止、アウトプット数、検証手段、孤立ノードなどを確認します。[ベンチマーク](./skills/theory-of-change-agent/benchmark/)では 18 件の違反をすべて検出しました。
- **アウトカム確認:** アウトカムが原因に働きかける変化かを確認し、指標には IRIS+ 593 指標から近い候補を参考として提示します。公式の対応付けではありません。
- **予算計算:** 合計、比率、資金分担、一般管理費上限はスクリプトが計算・検証します。実際の予算書で検証済みです。
- **推奨ルール:** SMART、CREAM、性別分解指標は採点のみです。採用するかどうかは利用者が決めます。

## データポリシー

- `docs/` にはセオリー・オブ・チェンジの参考資料など、公開文書だけを収録しています。
- `benchmark/` の PDM は架空の事例です。実名や実際の金額は含めません。
- 実際の事業 PDM や予算原本は、このリポジトリに保存しません。

## ステータス

バージョン 1.0 は国際開発協力、インパクトスタートアップ、CSR・ESG、非営利を対象にしています。
3 種類の進め方、品質ゲート、予算機能、HWP 入力、プラグイン配布を含みます。インパクト投資の審査機能は準備中です。

## ライセンス

[MIT](./LICENSE) © 2026 IMPACT SQUARE.
