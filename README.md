
Experiments around ToT. Includes:
- A base implementation of ToT (similar to Yao et al 2023)
- An implementation of ToT with BVSR for more creative branching


Problem set:
1. Which is greater, 9.9 or 9.11?
2. Just for fun, some problems from the ARC-AGI dataset. 


Models:
- Starting with Llama3.1 8B




Plan:
- Make an Ollama module. This module should wrap the Ollama python library, but also allow for branching, etc.
    - can Llama3.1/Ollama do forced JSON outputs?
- Replicate the base ToT implementation and run it on the 9.9 vs 9.11 problem.
- Create a BVSR module and extend the base ToT implementation with it.




Ideas:
- Does the model need the meta-skill of handling the tree? Currently the implementation is done by hand where I say look at these many branches, run the BVSR module, etc. Can the model learn to do it by itself? That is how humans do it anyway.
- How does this relate to process supervision?
- How do we solve/get around the Verifier problem? We need a strong verifier model to even tell us if an approach is correct.
- For a failed branch/CoT, can we summarize it so that other CoTs can learn from the mistake?
- Let the model be the memory gating function? Whether or not it should use lessons from failed CoTs should be up to the model?
- In BVSR, we can vary how unrelated the BV is. For the 9.9 vs. 9.11 problem, ideas could be related (e.g. in some way related to math), or unrelated (like a sci fi story idea). Can we get the LLM to 1. tag the problem so that related ideas can be generated from those tags and 2. somehow figure out a way to sample from the continuum from related to unrelated?