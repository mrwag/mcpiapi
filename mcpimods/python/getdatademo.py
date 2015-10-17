import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

p = mc.player.getTilePos()

for b in mc.getBlocks(p.x-2, p.y-2, p.z-2, p.x+2, p.y+2, p.z+2):
    print b

for b in mc.getBlocksWithData(p.x-2, p.y-2, p.z-2, p.x+2, p.y+2, p.z+2):
    print b
