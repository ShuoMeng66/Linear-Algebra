<div id="top"></div>

<!-- omit in toc -->
# 从零开始的线性代数教程

<p align="center">
  一个面向零基础、自学入门与补考复习的公开线性代数教材仓库，包含 LaTeX 源码、可直接阅读的 PDF、Cherry Studio 助教配置、学习 Agent 提示词，以及用于复核关键内容的校验脚本。
</p>

<p align="center">
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/graphs/contributors"><img src="https://img.shields.io/github/contributors/ShuoMeng66/Linear-Algebra.svg?style=for-the-badge" alt="Contributors"></a>
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/network/members"><img src="https://img.shields.io/github/forks/ShuoMeng66/Linear-Algebra.svg?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/stargazers"><img src="https://img.shields.io/github/stars/ShuoMeng66/Linear-Algebra.svg?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/issues"><img src="https://img.shields.io/github/issues/ShuoMeng66/Linear-Algebra.svg?style=for-the-badge" alt="Issues"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey.svg?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <a href="README.md"><strong>English</strong></a>
  ·
  <a href="dist/from_zero_linear_algebra.pdf"><strong>直接阅读 PDF</strong></a>
  ·
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/issues">反馈问题</a>
  ·
  <a href="https://github.com/ShuoMeng66/Linear-Algebra/issues">提出建议</a>
</p>

## 目录

- [关于项目](#关于项目)
- [技术与工具](#技术与工具)
- [快速开始](#快速开始)
- [使用方式](#使用方式)
- [仓库结构](#仓库结构)
- [路线图](#路线图)
- [参与贡献](#参与贡献)
- [许可说明](#许可说明)
- [联系方式](#联系方式)
- [致谢](#致谢)

## 关于项目

![教材封面预览](assets/images/preview/cover.png)

这个仓库围绕一份中文教材项目 `《从零开始的线性代数教程》` 展开。

它不是把线性代数拆成一堆互相脱节的定义，而是尽量按初学者更容易接受的顺序来讲：

```text
Gauss 消元与线性方程组
-> 矩阵基本运算
-> 特征值与相似对角化
-> 正交对角化
-> 二次型与正定矩阵
```

项目想做的事情很明确：让读者更容易起步，更容易复习，也更容易在卡题的时候继续往下走。

这个仓库现在同时提供：

- 一份适合直接阅读的 PDF 教材
- 一套完整的 LaTeX 源码，便于公开协作和长期维护
- Cherry Studio 助手订阅配置，以及可手动部署的学习 Agent
- 一个围绕本教材服务的助教 skill，而不是泛用数学聊天机器人
- 一个可复核部分例题、参数题和答案提示的校验脚本

### 为什么要做这个项目

- 很多同学第一次学线代，感受到的是概念堆叠，不是解题主线。
- 补考和临考复习更需要方法、常见题型和少丢分的提醒。
- 不少中文材料要么讲得太快，要么语言太硬，不太适合真正的初学者。

### 这个仓库的特点

- 章节主线稳定，不会随意发散到和当前学习目标关系不大的内容。
- 语言尽量自然，不故意写成很硬的教材腔。
- 会补更多常考的选择、填空和计算题，并尽量做严格校验。
- Cherry Studio 部分强调的是“伴学”和“讲清楚”，不是直接代做一切。

<p align="right">(<a href="#top">回到顶部</a>)</p>

## 技术与工具

- [XeLaTeX](https://www.latex-project.org/)：用于教材排版
- [Python](https://www.python.org/) 与 [SymPy](https://www.sympy.org/)：用于内容校验
- [Cherry Studio](https://docs.cherry-ai.com/cherry-studio/download)：用于部署教材助教和学习 Agent
- Markdown 与 JSON：用于文档、提示词和助手配置

<p align="right">(<a href="#top">回到顶部</a>)</p>

## 快速开始

### 运行前准备

- 已安装可用的 `xelatex`，例如 TeX Live 或 MiKTeX
- 如果要运行校验脚本，需要安装 Python 3 和 `sympy`
- 如果要使用 Cherry Studio 助教或 Agent，需要先安装 Cherry Studio

### 安装与编译

1. 克隆仓库。

   ```bash
   git clone git@github.com:ShuoMeng66/Linear-Algebra.git
   cd Linear-Algebra
   ```

2. 编译教材 PDF。

   ```bash
   cd src
   xelatex -interaction=nonstopmode -halt-on-error from_zero_linear_algebra.tex
   xelatex -interaction=nonstopmode -halt-on-error from_zero_linear_algebra.tex
   ```

3. 如有需要，把生成的 PDF 覆盖回 `dist/`。

   ```bash
   cp from_zero_linear_algebra.pdf ../dist/from_zero_linear_algebra.pdf
   ```

   如果你用的是 PowerShell，也可以写成：

   ```powershell
   Copy-Item from_zero_linear_algebra.pdf ..\dist\from_zero_linear_algebra.pdf
   ```

4. 如有需要，安装依赖并运行校验脚本。

   ```bash
   cd ..
   python -m pip install sympy
   python scripts/validate_content.py
   ```

<p align="right">(<a href="#top">回到顶部</a>)</p>

## 使用方式

### 直接阅读教材

如果你只是想先开始学，直接打开：

```text
dist/from_zero_linear_algebra.pdf
```

### 导入 Cherry Studio 助教

可以直接使用公开订阅文件：

```text
https://raw.githubusercontent.com/ShuoMeng66/Linear-Algebra/main/cherry-studio/assistants.json
```

相关文件：

- `cherry-studio/assistants.json`
- `skills/from-zero-linear-algebra-tutor/SKILL.md`

### 手动创建 Cherry Studio 学习 Agent

如果你更想要一个长期陪学的线代 Agent，可以看：

- `cherry-studio/agent-deployment.md`
- `cherry-studio/linear-algebra-learning-agent.prompt.md`

安全提醒：

- 权限模式只建议开 `普通模式` 或 `计划模式`
- 不要为这个学习型数学 Agent 开启 `全自动模式`

### 在修改内容后做一次校验

这个仓库提供了一个脚本，用来复核部分例题、参数题和答案提示：

```bash
python scripts/validate_content.py
```

### 这个仓库适合怎么用

- 自学入门
- 补考冲刺
- 课程讲义继续打磨
- Cherry Studio 教材伴学
- 后续继续扩展成更完整的公开教材项目

<p align="right">(<a href="#top">回到顶部</a>)</p>

## 仓库结构

```text
.
├─ assets/
├─ cherry-studio/
├─ dist/
├─ scripts/
├─ skills/
├─ src/
├─ CONTRIBUTING.md
├─ LICENSE
├─ README.md
├─ README-zh.md
├─ RELEASE_NOTES.md
└─ THIRD_PARTY_ASSETS.md
```

主要目录说明：

- `src/`：教材 LaTeX 源码
- `dist/`：编译好的 PDF 成品
- `scripts/`：内容校验脚本
- `cherry-studio/`：助手订阅、Agent 部署说明和提示词
- `skills/`：教材助教 skill 及其参考文件
- `assets/`：封面、预览图和其他视觉素材

<p align="right">(<a href="#top">回到顶部</a>)</p>

## 路线图

- [ ] 为高频考点继续补充经过严格校验的选择题、填空题和计算题
- [ ] 为每章最关键的题型补齐更完整的操作流程
- [ ] 继续扩充答案与讲解材料
- [ ] 做正式的 GitHub Releases，并附上对应 PDF
- [ ] 继续完善 Cherry Studio 助教的提示词、安全提示和学习流设计

更多想法和讨论可以看 [Issues](https://github.com/ShuoMeng66/Linear-Algebra/issues)。

<p align="right">(<a href="#top">回到顶部</a>)</p>

## 参与贡献

欢迎一起把这个项目打磨得更扎实，尤其欢迎下面这些方向的贡献：

- 纠正数学错误、表述不严谨和排版问题
- 补充更典型的三阶例题和经过核验的练习题
- 优化 Cherry Studio 助教提示词、陪学流程和部署文档
- 改善 public 仓库对读者和贡献者更友好的说明材料

提交前建议先看 [CONTRIBUTING.md](CONTRIBUTING.md)。  
如果涉及图片、Logo 或其他外部素材，也请先看 [THIRD_PARTY_ASSETS.md](THIRD_PARTY_ASSETS.md)。

<p align="right">(<a href="#top">回到顶部</a>)</p>

## 许可说明

这个仓库是公开的教材项目，但它 **不是** 常见的代码类 OSS 许可证仓库。

仓库中的原创教材文字、LaTeX 结构、教学性说明、Cherry Studio 提示词、助手配置和项目文档，采用：

- `CC BY-NC-SA 4.0`

使用前请特别注意：

- 需要保留署名
- 不允许直接用于商业用途
- 如果你基于原创内容继续公开改编，需保持相同或兼容的非商业共享协议
- 第三方图片、Logo 和外部来源视觉素材 **不在** 这份许可覆盖范围内

请在再发布、改编或二次使用前，认真查看 [LICENSE](LICENSE) 和 [THIRD_PARTY_ASSETS.md](THIRD_PARTY_ASSETS.md)。

<p align="right">(<a href="#top">回到顶部</a>)</p>

## 联系方式

ShuoMeng66

- GitHub: [@ShuoMeng66](https://github.com/ShuoMeng66)
- Email: `3067938917@qq.com`
- 项目地址: [https://github.com/ShuoMeng66/Linear-Algebra](https://github.com/ShuoMeng66/Linear-Algebra)

<p align="right">(<a href="#top">回到顶部</a>)</p>

## 致谢

- [Best README Template](https://github.com/othneildrew/Best-README-Template)
- [Cherry Studio 文档](https://docs.cherry-ai.com/)
- [SymPy](https://www.sympy.org/)

<p align="right">(<a href="#top">回到顶部</a>)</p>
