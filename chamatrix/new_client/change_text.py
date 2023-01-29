import aspose.words as aw

# load Word document
doc = aw.Document("static/test.docx")

# replace text
doc.range.replace("{{ a }}", "8", aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

# save the modified document
doc.save("static/test_updated.docx")
