# 贡献指南

欢迎你通过 Issue、Pull Request 或勘误建议参与这套线性代数教材的完善。

## 适合贡献的内容

- 纠正文中的数学错误、排版错误、错别字
- 优化章节顺序、例题解释、过渡段落
- 增加更典型的三阶矩阵例题
- 增加更适合补考复习的练习题与答案提示
- 改进 README、仓库结构与编译说明
- 改进 Cherry Studio 教材助教 skill 的提示词、章节映射、使用说明与示例问法

## 提交前请注意

1. 保持主线不变  
   请优先围绕以下主线贡献内容：  
   `Gauss 消元 -> 矩阵基本运算 -> 特征值分解 -> 正交对角化 -> 二次型与正定矩阵`

2. 优先照顾初学者  
   本教材面向零基础与补考同学，写作时请避免默认读者已经掌握抽象线性空间、公理化证明等更高阶背景。

3. 例题尽量典型  
   除非有特别必要，新增例题优先选择三阶矩阵或最能体现结构的例子，而不是过于理想化的二维特例。

4. 保持中文表达自然  
   解释应尽量清楚、平实、有逻辑，不要只把教材语言机械压缩成结论列表。

5. 不要随意加入来源不明的图片  
   如果要新增图片、Logo、角色图，请先确认来源与使用边界，并同步更新 [THIRD_PARTY_ASSETS.md](THIRD_PARTY_ASSETS.md)。

6. 修改 skill 时，保持“教材伴学”定位  
   `skills/` 和 `cherry-studio/` 下的内容不是泛用数学助手，而是围绕《从零开始的线性代数教程》服务的教材助教。修改时请优先保持以下场景：
   - 解释“这本书某个例题是怎么来的”
   - 把某个知识点讲得更细、更基础
   - 提供更多同类型三阶例题
   - 解释证明题里“某一步为什么成立”
   - 检查学生自己的证明、计算过程和半成品思路
   - 在学生卡住时按提示粒度逐步引导
   - 处理 OCR 文本、凌乱草稿和错题复盘
   - 面向补考同学做重点梳理与易错点提醒

7. 修改 skill 时，默认照顾零基础读者  
   skill 的提示词、示例问题和回答框架应尽量避免 AI 圈黑话、提示词工程术语和过度抽象的数学表达。目标读者通常只关心“怎么学懂、怎么解题、怎么少丢分”。

8. 修改 skill 后要同步相关文件  
   如果你修改了教材助教的定位、回答方式、示例或部署流程，请至少检查这些文件是否需要一起更新：
   - [README.md](README.md)
   - [cherry-studio/assistants.json](cherry-studio/assistants.json)
   - [skills/from-zero-linear-algebra-tutor/SKILL.md](skills/from-zero-linear-algebra-tutor/SKILL.md)
   - [skills/from-zero-linear-algebra-tutor/references/chapter_map.md](skills/from-zero-linear-algebra-tutor/references/chapter_map.md)
   - [skills/from-zero-linear-algebra-tutor/references/coaching_workflows.md](skills/from-zero-linear-algebra-tutor/references/coaching_workflows.md)
   - [skills/from-zero-linear-algebra-tutor/references/response_patterns.md](skills/from-zero-linear-algebra-tutor/references/response_patterns.md)
   - [skills/from-zero-linear-algebra-tutor/references/system_prompt.md](skills/from-zero-linear-algebra-tutor/references/system_prompt.md)

## 文件结构约定

```text
.
├─ README.md
├─ LICENSE
├─ CONTRIBUTING.md
├─ THIRD_PARTY_ASSETS.md
├─ cherry-studio/
├─ skills/
├─ src/
├─ dist/
└─ assets/
```

- `src/` 放 LaTeX 源码
- `dist/` 放可直接阅读的 PDF 成品
- `assets/` 放图片资源与 README 预览图
- `cherry-studio/` 放可直接订阅的助手配置
- `skills/` 放教材助教 skill 本体与参考资料

## 关于 Cherry Studio skill 的贡献建议

如果你准备改教材助教 skill，建议优先遵守下面几条：

1. 不要把它改成“泛用线性代数机器人”  
   它的核心价值在于贴合本教材的主线和讲法，而不是追求覆盖所有线代话题。

2. 回答结构要稳定  
   skill 应优先支持以下几类提问：
   - 例题来源与例题精讲
   - 知识点细化讲解
   - 同类题扩展
   - 证明题某一步解释
   - 学生思路检查与最小修改
   - 做到一半后的提示式引导
   - OCR 文本整理与继续讲解
   - 补考复习模式

3. 例子优先用三阶矩阵  
   除非是为了做最基础的热身说明，否则请尽量维持本仓库“例题以三阶矩阵为主”的风格。

4. 不要把模型密钥、个人接口地址写进仓库  
   `assistants.json` 只能放公开可分发的助手配置，不能写入个人 API Key、私有网关或带敏感信息的链接。

5. 修改后至少做两项检查  
   - 检查 `assistants.json` 是否仍是合法 JSON
   - 检查 README 中的部署流程、模型建议、订阅地址、示例问法和批改类用法是否仍然匹配

## 编译检查

提交涉及 LaTeX 正文的修改前，建议至少完成一次双编译：

```bash
cd src
xelatex -interaction=nonstopmode -halt-on-error from_zero_linear_algebra.tex
xelatex -interaction=nonstopmode -halt-on-error from_zero_linear_algebra.tex
```

如果你更新了 PDF 成品，请同步覆盖：

```bash
copy from_zero_linear_algebra.pdf ..\\dist\\from_zero_linear_algebra.pdf
```

## Pull Request 建议

- 标题尽量直接说明改动范围，例如：`补充第三章重根不可对角化例题`
- 描述里说明：
  - 改了什么
  - 为什么要改
  - 是否重新编译 PDF
  - 是否新增或替换了第三方素材
  - 如果涉及 skill，是否同步更新了 `README`、`assistants.json` 和 `skills/` 下的参考文件

## 不建议直接改动的内容

- 未经说明大幅改变全书主线
- 随意删除已经成体系的基础讲解
- 未核实版权就新增外部图片
- 提交 `aux/log/toc/synctex` 等中间文件
