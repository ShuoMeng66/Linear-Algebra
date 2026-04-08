# 面试速记：项目细节与考点收拢

这是面向技术面试的项目速记，重点覆盖“项目结构、关键实现、可讨论点、风险与取舍”。

## 项目定位

- 开源中文线性代数讲义，面向零基础与补考
- 主线结构：方程组 -> 矩阵运算 -> 相似对角化 -> 正交对角化 -> 二次型
- 形式：LaTeX 主文档 + 生成 PDF
- 增强：Cherry Studio 助手订阅 + 手动部署学习 Agent + 教材助教 skill

## 仓库结构与职责分工

- `src/from_zero_linear_algebra.tex`  
主讲义源码，全部数学内容、例题、习题、答案提示都在这里
- `dist/from_zero_linear_algebra.pdf`  
编译出的可直接阅读 PDF
- `cherry-studio/assistants.json`  
Cherry Studio 订阅配置，包含“教材助教”和“学习 Agent”
- `cherry-studio/agent-deployment.md`  
手动创建 Agent 的操作说明
- `cherry-studio/linear-algebra-learning-agent.prompt.md`  
学习 Agent 提示词正文
- `skills/from-zero-linear-algebra-tutor/`  
教材助教 skill，包含 SKILL.md + references
- `scripts/validate_content.py`  
用 sympy 校验关键例题、参数题与答案提示
- `README.md`  
部署、使用、模型建议、Agent 安全注意事项

## 关键内容改动与亮点

- 修正讲义中已核对的数学错误（第 1 章两处答案提示错误）
- 每章新增“选择/填空快练”和速判技巧
- 第 4 章新增“正交对角化 = 相似对角化的特殊情况”说明
- 第 4 章新增 Gram-Schmidt 正交化 + 单位化完整流程和示例
- 增加脚本校验（sympy），降低内容错误风险
- Cherry Studio 增加两条部署路线：订阅助手 + 手动创建 Agent
- 强化安全提示：Agent 权限模式只建议普通或计划模式，不建议全自动

## 可讲的技术点与设计取舍

- **为什么从方程组开始**  
强调“解方程”是线性代数最直观入口，减少概念堆叠
- **A/B/C 分级习题**  
便于补考、分层训练，题型与难度递进
- **选择/填空快练**  
补齐考试高频题型，强调速判规则
- **内容校验脚本**  
用可执行脚本保障数学结论，降低文本维护风险
- **双路线 Agent 部署**  
订阅方式适合用户直接用，手动方式适合定制
- **安全建议明确**  
Agent 用途是教学，不应开启高权限或全自动

## 可被追问的具体细节

- “正交对角化为什么是相似对角化的特殊情况”  
关键在标准正交特征向量组：`Q^{-1} = Q^T`
- “重特征值怎么处理”  
同一特征空间内部做 Gram-Schmidt，先正交化再单位化
- “为什么要引入校验脚本”  
数学内容可被误抄/误算，脚本可复核关键答案提示
- “为什么不用 OCR 批量引入题库”  
原始 PDF 质量差，OCR 错误率高，宁可精选校验题型
- “Cherry Studio Agent 安全策略”  
普通/计划模式即可，避免全自动带来的本地风险

## 面试题式问答准备

- Q: 你如何保证讲义数学正确性？  
  A: 用 `scripts/validate_content.py` 对关键例题、参数分类和答案提示做符号校验，保持内容可回归验证。
- Q: 第 4 章为什么要加 Gram-Schmidt？  
  A: 正交对角化在重特征值时必须在同一特征空间内正交化，Gram-Schmidt 是最稳流程。
- Q: 你如何照顾初学者？  
  A: 先讲人话再定义、加“快练/速判”、问题驱动而非术语堆砌。
- Q: 为什么同时提供助手订阅和手动 Agent？  
  A: 订阅最快速可用，手动 Agent 更可控、可自定义模型与权限。
- Q: 为什么特别强调权限模式？  
  A: 教学场景无必要高权限，安全风险不值。

## 编译与验证

- 校验脚本：
```bash
python scripts/validate_content.py
```
- PDF 编译：
```bash
cd src
xelatex -interaction=nonstopmode -halt-on-error from_zero_linear_algebra.tex
xelatex -interaction=nonstopmode -halt-on-error from_zero_linear_algebra.tex
```

## 面试加分点建议

- 强调“教育产品”的可用性：步骤清晰、风格温和、错误可验证
- 强调“内容即代码”的工程化：有版本、有回归校验、有发布流程
- 强调“安全边界”：教学 Agent 不做系统级操作
