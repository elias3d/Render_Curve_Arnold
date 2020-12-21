#All NURBS' Drawing Overrides Color should be set as RGB

import maya.cmds as cmds
CurveWidth = 0.1
countLayer=1
index=0
lSelection = cmds.ls(sl = True)
lShapes = cmds.listRelatives(lSelection, s=True, fullPath = True)
print lShapes

for index in range(0,len(lShapes)) :
    curveI = lShapes[index]
    cmds.setAttr(curveI + '.aiRenderCurve', 1 )
    cmds.setAttr(curveI + '.aiCurveWidth', CurveWidth )
    cmds.setAttr(curveI + '.castsShadows', 0)
    cmds.setAttr(curveI + '.aiMatte', 0)
    cmds.setAttr(curveI + '.aiExportRefPoints', 0)
    cmds.setAttr(curveI + '.aiOpaque', 1)
    cmds.setAttr(curveI + '.aiVisibleInDiffuseReflection', 0)
    cmds.setAttr(curveI + '.aiVisibleInSpecularReflection', 0)
    cmds.setAttr(curveI + '.aiVisibleInDiffuseTransmission', 0)
    cmds.setAttr(curveI + '.aiVisibleInSpecularTransmission', 0)
    cmds.setAttr(curveI + '.aiVisibleInVolume', 0)
    cmds.setAttr(curveI + '.aiSelfShadows', 0)
    cmds.setAttr(curveI + '.aiMode', 1)
    colorNode = cmds.shadingNode('multiplyDivide', asUtility=1)
    print curveI
    cmds.connectAttr(curveI + '.overrideColorRGB', colorNode + '.input1')
    cmds.connectAttr(colorNode + '.output', curveI + '.aiCurveShader')

    
    index = index +1
countLayer = countLayer +1