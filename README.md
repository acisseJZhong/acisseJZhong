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


<!-- RECENT_CONTRIBUTIONS_START -->
### Recent Contributions

#### [pytorch/torchtitan](https://github.com/pytorch/torchtitan)

| Date | PR | Summary |
|------|-----|---------|
| 2026-03-24 | [#2680](https://github.com/pytorch/torchtitan/pull/2680) | **[RL] Add parallelism plan for qwen3 30B-A3B MoE to run e2e** — [RL] Add parallelism plan for qwen3 30B-A3B MoE to run e2e |
| 2026-03-20 | [#2638](https://github.com/pytorch/torchtitan/pull/2638) | **[RL] adopt local map attention for vLLM attention** — Adopt LocalMapAttention as the base class for VLLMAttention, replacing manual DTensor.to_local() / DTensor.from_local() with local_map for DTensor-to- |
| 2026-03-18 | [#2625](https://github.com/pytorch/torchtitan/pull/2625) | **[Draft WIP] MoE with LocalMap** — [Draft WIP] MoE with LocalMap |
| 2026-03-17 | [#2615](https://github.com/pytorch/torchtitan/pull/2615) | **[Module] Modularize MoE components** — GroupedExperts inherits from Module with a nested Config dataclass. dim, hidden_dim, and num_experts use field(init=False) so they are set at build() |
| 2026-03-17 | [#2613](https://github.com/pytorch/torchtitan/pull/2613) | **[Module] Modularize MoE components** — GroupedExperts inherits from Module with a nested Config dataclass. dim, hidden_dim, and num_experts use field(init=False) so they are set at build() |
| 2026-03-13 | [#2571](https://github.com/pytorch/torchtitan/pull/2571) | **[Module] Modularize MoE components** — GroupedExperts inherits from Module with a nested Config dataclass. dim, hidden_dim, and num_experts use field(init=False) so they are set at build() |
| 2026-03-13 | [#2567](https://github.com/pytorch/torchtitan/pull/2567) | **[rl] Refactor Episode definition to be a single completion instead of a group (#2529)** — Previously we use `Episode` to represent a group of completion in |
| 2026-03-11 | [#2557](https://github.com/pytorch/torchtitan/pull/2557) | **Adopt Local Map Wrapper for Inner Attention** — Add _InnerAttentionBase base class to attention.py — overrides `__call__` to wrap `nn.Module.__call__` with local_map, converting TP DTensor inputs to |

[View all my PRs in pytorch/torchtitan &rarr;](https://github.com/pytorch/torchtitan/pulls?q=is%3Apr+author%3AacisseJZhong)

#### [pytorch/pytorch](https://github.com/pytorch/pytorch)

| Date | PR | Summary |
|------|-----|---------|
| 2026-02-26 | [#175867](https://github.com/pytorch/pytorch/pull/175867) | **[DTensor] Add grad_placement to from_local** — While fixing a MoE numerics bug (pytorch/torchtitan#2416), we discovered the root cause was a lack of strict gradient placement control/strict typing |
| 2026-01-27 | [#173454](https://github.com/pytorch/pytorch/pull/173454) | **[DTensor] Fix `to_local` backward by providing default `grad_placement` type** — Fixes #172932, see comment here |
| 2026-01-23 | [#173153](https://github.com/pytorch/pytorch/pull/173153) | **[DTensor][BE] redistribute to replicate in from_local backward for partial target type** — follow up per this comment |
| 2025-12-16 | [#170527](https://github.com/pytorch/pytorch/pull/170527) | **[DTensor] Provide user control of output gradients placements** — As discussed in https://github.com/pytorch/pytorch/pull/170147(see comment here and here), we added a parameter `grad_placements` to `from_local` and |
| 2025-12-15 | [#170423](https://github.com/pytorch/pytorch/pull/170423) | **[BE] Rename MaskPartial back to _MaskPartial** — `MaskPartial` was made to a public class in https://github.com/pytorch/pytorch/pull/164414, this PR changes it back to a private class, as this class |
| 2025-12-13 | [#170356](https://github.com/pytorch/pytorch/pull/170356) | **make redistribute bwd no-op if fwd is no-op** — make redistribute bwd no-op if fwd is no-op |
| 2025-12-13 | [#170355](https://github.com/pytorch/pytorch/pull/170355) | **[DTensor][BE] remove is_backward from redistribute_local_tensor** — 1. remove the `is_backward` parameter from `redistribute_local_tensor`, instead, do the backward conversion before we call `redistribute_local_tensor` |
| 2025-12-11 | [#170147](https://github.com/pytorch/pytorch/pull/170147) | **[DTensor][BE] remove is_backward from redistribute_local_tensor** — 1. remove the `is_backward` parameter from `redistribute_local_tensor`, instead, do the backward conversion before we call `redistribute_local_tensor` |

[View all my PRs in pytorch/pytorch &rarr;](https://github.com/pytorch/pytorch/pulls?q=is%3Apr+author%3AacisseJZhong)

#### [vllm-project/vllm](https://github.com/vllm-project/vllm)

| Date | PR | Summary |
|------|-----|---------|
| 2025-09-29 | [#25912](https://github.com/vllm-project/vllm/pull/25912) | **[BugFix] Pass config_format via try_get_generation_config** — Fixed a bug when using customized config parser: we need to pass in `self.config_format`. |

[View all my PRs in vllm-project/vllm &rarr;](https://github.com/vllm-project/vllm/pulls?q=is%3Apr+author%3AacisseJZhong)

#### [meta-pytorch/torchtune](https://github.com/meta-pytorch/torchtune)

| Date | PR | Summary |
|------|-----|---------|
| 2025-02-10 | [#2377](https://github.com/meta-pytorch/torchtune/pull/2377) | **Fix Qwen config** — What is the purpose of this PR? Is it to |
| 2025-02-07 | [#2362](https://github.com/meta-pytorch/torchtune/pull/2362) | **[Fix Test] Fix failed generation test by pining pytorch nightlies** — What is the purpose of this PR? Is it to |
| 2025-02-06 | [#2351](https://github.com/meta-pytorch/torchtune/pull/2351) | **Fix saving adapter weights after disabling DSD** — What is the purpose of this PR? Is it to |
| 2025-02-05 | [#2346](https://github.com/meta-pytorch/torchtune/pull/2346) | **[Bug Fix]Disable DSD for saving ckpt** — What is the purpose of this PR? Is it to |
| 2025-02-02 | [#2330](https://github.com/meta-pytorch/torchtune/pull/2330) | **TP + FSDP distributed training (full finetuning)** — What is the purpose of this PR? Is it to |
| 2025-02-01 | [#2328](https://github.com/meta-pytorch/torchtune/pull/2328) | **Add distributed inference for llama3.2 vision** — What is the purpose of this PR? Is it to |
| 2025-01-29 | [#2317](https://github.com/meta-pytorch/torchtune/pull/2317) | **fix state dict hook for early fusion models** — What is the purpose of this PR? Is it to |
| 2025-01-13 | [#2260](https://github.com/meta-pytorch/torchtune/pull/2260) | **Fix tests due to upgrade to cuda126** — What is the purpose of this PR? Is it to |
| 2025-01-13 | [#2259](https://github.com/meta-pytorch/torchtune/pull/2259) | **Downgrade cuda to 12.4** — What is the purpose of this PR? Is it to |
| 2025-01-10 | [#2245](https://github.com/meta-pytorch/torchtune/pull/2245) | **Added Distributed(Tensor Parallel) Inference Recipe** — What is the purpose of this PR? Is it to |

[View all my PRs in meta-pytorch/torchtune &rarr;](https://github.com/meta-pytorch/torchtune/pulls?q=is%3Apr+author%3AacisseJZhong)

_Last updated: 2026-03-24 10:10 UTC_
<!-- RECENT_CONTRIBUTIONS_END -->

