### Hey, I'm [Jessica Zhong!](https://github.com/acisseJZhong)

![](https://visitor-badge.laobi.icu/badge?page_id=acisseJZhong.acisseJZhong)

I'm a software engineer passionate about ML infrastructure, large-scale model training, and LLM serving systems.

- Working on PyTorch-based training and inference infrastructure
- Contributing to open-source ML frameworks

**Organizations & Key Projects:**

| Project | Description |
|---------|-------------|
| [PyTorch](https://github.com/pytorch/pytorch) | Core contributor to the deep learning framework |
| [torchtune](https://github.com/meta-pytorch/torchtune) | PyTorch native post-training library for LLMs |
| [torchtitan](https://github.com/pytorch/torchtitan) | PyTorch native platform for training generative AI models |
| [vLLM](https://github.com/vllm-project/vllm) | High-throughput and memory-efficient LLM inference engine |

---

![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=acisseJZhong&theme=vue)

![](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=acisseJZhong&theme=vue)
![](https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=acisseJZhong&theme=vue)

![](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=acisseJZhong&theme=vue)
![](https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=acisseJZhong&theme=vue&utcOffset=-8)

---

**Pinned Repositories:**

<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="50%"><a href="https://github.com/pytorch/torchtitan"><img width="100%" src="https://github-readme-stats.vercel.app/api/pin/?username=pytorch&repo=torchtitan&theme=default&description_lines_count=2" /></a></td>
<td width="50%"><a href="https://github.com/pytorch/pytorch"><img width="100%" src="https://github-readme-stats.vercel.app/api/pin/?username=pytorch&repo=pytorch&theme=default&description_lines_count=2" /></a></td>
</tr>
<tr>
<td width="50%"><a href="https://github.com/vllm-project/vllm"><img width="100%" src="https://github-readme-stats.vercel.app/api/pin/?username=vllm-project&repo=vllm&theme=default&description_lines_count=2" /></a></td>
<td width="50%"><a href="https://github.com/meta-pytorch/torchtune"><img width="100%" src="https://github-readme-stats.vercel.app/api/pin/?username=meta-pytorch&repo=torchtune&theme=default&description_lines_count=2" /></a></td>
</tr>
</table>

---

### Recent Contributions

#### [pytorch/torchtitan](https://github.com/pytorch/torchtitan)

| Date | PR | Summary |
|------|-----|---------|
| 2026-03-20 | [#2638](https://github.com/pytorch/torchtitan/pull/2638) | **[RL] Adopt LocalMapAttention for vLLM attention** — Replace base class for VLLMAttention with LocalMapAttention |
| 2026-03-18 | [#2625](https://github.com/pytorch/torchtitan/pull/2625) | **[Draft WIP] MoE with LocalMap** |
| 2026-03-17 | [#2615](https://github.com/pytorch/torchtitan/pull/2615) | **[Module] Modularize MoE components** — Continues modularization effort for Embedding, RMSNorm, and Linear; makes MoE components reusable |
| 2026-03-13 | [#2567](https://github.com/pytorch/torchtitan/pull/2567) | **[RL] Refactor Episode definition** — Refactor Episode to represent a single completion instead of a group |
| 2026-03-11 | [#2557](https://github.com/pytorch/torchtitan/pull/2557) | **Adopt Local Map Wrapper for Inner Attention** — Continuation of local map attention integration work |
| 2026-03-09 | [#2532](https://github.com/pytorch/torchtitan/pull/2532) | **[DTensor Bugfix] Fix grad_placements in to_local** — Explicitly specify grad_placements to ensure necessary all-reduce takes place on multi-dimensional DTensors |

#### [pytorch/pytorch](https://github.com/pytorch/pytorch)

| Date | PR | Summary |
|------|-----|---------|
| 2026-02-26 | [#175867](https://github.com/pytorch/pytorch/pull/175867) | **[DTensor] Add grad_placement to from_local** — Add strict gradient placement control to fix MoE numerics bug |
| 2026-01-27 | [#173454](https://github.com/pytorch/pytorch/pull/173454) | **[DTensor] Fix to_local backward** — Fix DTensor.to_local() backward by providing default grad_placement type |
| 2026-01-23 | [#173153](https://github.com/pytorch/pytorch/pull/173153) | **[DTensor] Redistribute to replicate in from_local backward** — Handle partial target type in from_local backward |
| 2025-12-16 | [#170527](https://github.com/pytorch/pytorch/pull/170527) | **[DTensor] User control of output gradient placements** — Provide user control over output gradient placements in DTensor |
| 2025-12-15 | [#170423](https://github.com/pytorch/pytorch/pull/170423) | **Rename MaskPartial back to _MaskPartial** — Revert MaskPartial to private class |
| 2025-12-13 | [#170355](https://github.com/pytorch/pytorch/pull/170355) | **[DTensor] Remove is_backward from redistribute_local_tensor** — Clean up backward-specific logic from redistribute |
| 2025-12-11 | [#170147](https://github.com/pytorch/pytorch/pull/170147) | **[DTensor] Remove is_backward from redistribute_local_tensor** — Refactor to do backward conversion before calling redistribute_local_tensor |

#### [vllm-project/vllm](https://github.com/vllm-project/vllm)

| Date | PR | Summary |
|------|-----|---------|
| 2025-09-29 | [#25912](https://github.com/vllm-project/vllm/pull/25912) | **[BugFix] Pass config_format via try_get_generation_config** — Fix bug when using customized config parser by passing in config_format |

#### [meta-pytorch/torchtune](https://github.com/meta-pytorch/torchtune)

| Date | PR | Summary |
|------|-----|---------|
| 2025-02-10 | [#2377](https://github.com/meta-pytorch/torchtune/pull/2377) | **Fix Qwen config** — Bug fix for Qwen model configuration |
| 2025-02-07 | [#2362](https://github.com/meta-pytorch/torchtune/pull/2362) | **[Fix Test] Fix failed generation test** — Pin pytorch nightlies to fix generation test |
| 2025-02-06 | [#2351](https://github.com/meta-pytorch/torchtune/pull/2351) | **Fix saving adapter weights after disabling DSD** — Bug fix for checkpoint saving |
| 2025-02-05 | [#2346](https://github.com/meta-pytorch/torchtune/pull/2346) | **[Bug Fix] Disable DSD for saving checkpoint** — Fix checkpoint saving with DSD disabled |
| 2025-02-02 | [#2330](https://github.com/meta-pytorch/torchtune/pull/2330) | **TP + FSDP distributed training (full finetuning)** — Add tensor parallel + FSDP support for full finetuning |
| 2025-02-01 | [#2328](https://github.com/meta-pytorch/torchtune/pull/2328) | **Add distributed inference for Llama 3.2 Vision** — New feature for distributed inference on vision models |
| 2025-01-29 | [#2317](https://github.com/meta-pytorch/torchtune/pull/2317) | **Fix state dict hook for early fusion models** — Bug fix for early fusion model state dicts |
| 2025-01-10 | [#2245](https://github.com/meta-pytorch/torchtune/pull/2245) | **Added Distributed (Tensor Parallel) Inference Recipe** — New tensor parallel inference recipe |
