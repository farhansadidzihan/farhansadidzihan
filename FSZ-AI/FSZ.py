import replicate

# output = replicate.run(
#   "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
#   input={"prompt": "an iguana on the beach, pointillism"}
# )

# for item in output:
#     print(item, end="")

iterator = replicate.run(
  "mistralai/mixtral-8x7b-instruct-v0.1",
  input={"prompt": "Who was Dolly the sheep?"},
)
for text in iterator:
      print(text)