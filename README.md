# AgentHarnessLab

**免费 Agent Harness 工程实战课：手把手构建你的第一个 Agent Harness 应用。**

使用 **Python + uv + DeepSeek**，从最小工具调用开始，逐步实现执行循环、上下文管理、会话恢复、多 Agent 协作与评测。共 **20 篇**，在同一个项目中持续开发。

**文章、完整代码与学习笔记全部免费。** 正文讲核心实现，配套源码提供完整示例。

[课程目录](docs/articles/README.md) · [第一篇：从读懂到动手](<docs/articles/01 从读懂到动手：用 Python 构建一个能读懂项目的 Agent.md>) · [工程架构](docs/architecture.md)

## 适合人群

| 人群 | 学习目标 |
| --- | --- |
| 程序员转型 AI 应用开发 | 将已有开发经验迁移到模型接入、工具编排和 Agent 运行机制。 |
| 在校学生与应届毕业生 | 完成有代码、测试与演示的项目，用于作品集、实习和面试。 |
| AI 产品经理及转型中的产品经理 | 理解 Agent 的能力、权限、失败处理与验收方式。 |
| 独立开发者与技术创业者 | 构建可扩展的 Agent Harness 应用，验证业务任务的效果与成本。 |
| Agent 初学者 | 从一次工具调用理解 Agent 如何获取信息、执行任务并交付结果。 |

无需 Agent 开发经验。动手实战需要基础 Python、终端操作和 Git；产品经理可先阅读流程与验收部分。

## 课程内容

| 章节 | 内容 | 阶段成果 |
| --- | --- | --- |
| 01—04 基础篇 | 模型接入、工具调用、执行循环、能力装配 | 跑通最小 Agent |
| 05—08 核心篇 | 工具设计、执行环境、Skills、MCP、上下文管理 | 使用真实工具完成任务 |
| 09—12 会话篇 | 持久化、压缩、中断恢复、长期记忆 | 支持可追溯、可恢复的长任务 |
| 13—16 编排篇 | 目标拆解、工作流、角色权限、子任务协作 | 实现受控的多 Agent 协作 |
| 17—20 落地篇 | 评测、调用追踪、失败恢复、安全与经验更新 | 验证效果、定位问题并持续改进 |

## 学完能掌握哪些能力

| 能力方向 | 核心技术与实战成果 |
| --- | --- |
| 模型接入 | 接入 DeepSeek Provider，处理 Function Calling、Streaming 流式输出、工具参数拼接、超时与调用错误。 |
| Agent 运行机制 | 实现 Agent Loop，管理 Model、Context、State，串联模型请求、工具执行、结果回传与停止条件。 |
| 工具与执行环境 | 定义 Tool Schema 和结构化结果，接入 Shell、Browser、Skills 与 MCP，处理参数校验、审批和沙箱隔离。 |
| 上下文与会话 | 实现 Session 事件日志、状态重建、Context Compaction、Checkpoint / Resume，处理恢复时的重复执行风险及长期记忆更新。 |
| 工作流与协作 | 使用 Goal、Plan 拆解任务，通过 Workflow 管理依赖，以 Preset 配置角色与权限，实现 Subagent 委派、并发控制、预算与取消传播。 |
| 可靠性与评测 | 通过调用追踪定位失败，统计 Token、耗时与成本；建立固定评测集，验证模型、Prompt 和 Skill 的修改，设计 Retry 与失败恢复策略。 |
| 安全与权限 | 区分用户指令与外部资料，防范 Prompt Injection，落实最小权限、工具审批、执行隔离与数据访问控制。 |
| AI 辅助研发 | 使用 AI 编写代码，独立完成 Code Review、测试和问题定位，判断实现质量与运行风险。 |

完成实战后，可将自己的实现、演示和验证结果整理为简历项目，并结合代码准备工具调用、状态恢复、权限控制和评测等面试问题。

![课程相关配图](https://img-1312281807.cos.ap-guangzhou.myqcloud.com/img/708c1c5aff6cea7f83134ed3aa63e715.png)

## 开始学习

**运行参考代码：** 安装 [uv](https://docs.astral.sh/uv/getting-started/installation/) 后执行：

```bash
git clone https://github.com/anxiong2025/AgentHarnessLab.git
cd AgentHarnessLab
uv sync --locked
uv run python -m agent_harness_lab.first_agent --help
uv run python examples/01-project-reader/check_tools.py
```

以上命令无需 API Key。真实模型调用需要自己的 DeepSeek 凭据，API 费用由服务商收取；配置和运行方法见文章。

## 当前进度

### 基础篇：先跑通，再理解运行骨架

- [x] 01｜最小实战：完成一次工具调用与任务交付
- [ ] 02｜模型接入：DeepSeek、Function Calling 与流式输出
- [ ] 03｜行动闭环：Model、Context 与 Agent Loop
- [ ] 04｜能力装配：Python 接口、依赖注入与生命周期

### 核心篇：让 Agent 使用真实工具与环境

- [ ] 05｜工具设计：Schema、结构化结果与错误处理
- [ ] 06｜安全执行：Shell、沙箱与审批
- [ ] 07｜能力扩展：Browser、Skills 与 MCP
- [ ] 08｜上下文管理：历史消息、工具结果与信息选择

### 会话篇：让长任务可追溯、可恢复

- [ ] 09｜会话持久化：事件日志、状态投影与成果存储
- [ ] 10｜上下文压缩：Compaction 与信息保留
- [ ] 11｜中断恢复：Checkpoint、Resume 与执行状态
- [ ] 12｜长期记忆：跨任务检索、更新与遗忘

### 编排篇：从单 Agent 到有序协作

- [ ] 13｜目标拆解：Goal、Plan 与动态任务树
- [ ] 14｜流程调度：Workflow、依赖与停止条件
- [ ] 15｜角色装配：Preset、Prompt 与工具权限
- [ ] 16｜并行协作：Subagent、预算与结果汇总

### 落地篇：验证可靠性，形成改进闭环

- [ ] 17｜结果验证：完成判定、评测与回归测试
- [ ] 18｜失败恢复：调用追踪、成本、重试与停止策略
- [ ] 19｜安全加固：最小权限、隔离与 Prompt Injection 防护
- [ ] 20｜经验更新：复盘、Skill 改进、评测与回滚

## 项目结构

```text
src/agent_harness_lab/   应用代码
examples/               示例文件与演示
tests/                  自动化测试
docs/articles/          课程文章与笔记
pyproject.toml          项目与依赖配置
uv.lock                 依赖锁文件
```

[贡献指南](CONTRIBUTING.md) · [反馈问题](https://github.com/anxiong2025/AgentHarnessLab/issues)

## 开源协议

本项目的代码、课程文章与学习笔记采用 [MIT License](LICENSE)。允许使用、修改、分发和商业使用，需保留版权声明及许可文本。第三方引用内容与素材遵循其原有许可。
