# TOOLS OWNER : MD SAMIUL ISLAM
#----------------------------------------------
import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))