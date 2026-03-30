# 贡献指南

欢迎你通过 Issue、Pull Request 或勘误建议参与这套线性代数教材的完善。

## 适合贡献的内容

- 纠正文中的数学错误、排版错误、错别字
- 优化章节顺序、例题解释、过渡段落
- 增加更典型的三阶矩阵例题
- 增加更适合补考复习的练习题与答案提示
- 改进 README、仓库结构与编译说明

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

## 文件结构约定

```text
.
├─ README.md
├─ LICENSE
├─ CONTRIBUTING.md
├─ THIRD_PARTY_ASSETS.md
├─ src/
├─ dist/
└─ assets/
```

- `src/` 放 LaTeX 源码
- `dist/` 放可直接阅读的 PDF 成品
- `assets/` 放图片资源与 README 预览图

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

## 不建议直接改动的内容

- 未经说明大幅改变全书主线
- 随意删除已经成体系的基础讲解
- 未核实版权就新增外部图片
- 提交 `aux/log/toc/synctex` 等中间文件
