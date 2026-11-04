# 全书最终自动审计

状态：自动检查通过（不代替忠实性及目视审阅）.

MAIN：`Optimal Transport for Applied Mathematicians_Chn.tex`
PDF：`Optimal Transport for Applied Mathematicians_Chn.pdf`

输入文件：56；PDF物理页数：339.
底本SHA256：`7820e876d4312d7355f0a1549b2af2186594eebef8d411d651c6235b8c119b68`.

## 实际链接分段比较

|部分|原PDF物理页|译稿物理页|原内部链接|相关基线|译稿内部链接|状态|
|---|---|---|---:|---:|---:|---|
|front|[1, 28]|[1, 24]|197|197|423|passed-count-baseline|
|chapter1|[29, 85]|[25, 74]|209|209|216|passed-count-baseline|
|chapter2|[86, 112]|[75, 97]|80|79|79|passed-count-baseline|
|chapter3|[113, 145]|[98, 126]|118|118|119|passed-count-baseline|
|chapter4|[146, 200]|[127, 173]|244|244|288|passed-count-baseline|
|chapter5|[201, 242]|[174, 208]|187|187|191|passed-count-baseline|
|chapter6|[243, 272]|[209, 235]|125|125|127|passed-count-baseline|
|chapter7|[273, 308]|[236, 265]|117|117|119|passed-count-baseline|
|chapter8|[309, 347]|[266, 298]|160|160|162|passed-count-baseline|
|exercises|[348, 357]|[299, 308]|15|15|15|passed-count-baseline|
|hints|[358, 361]|[309, 312]|14|14|83|passed-count-baseline|
|bibliography|[362, 373]|[313, 335]|0|0|0|passed-count-baseline|
|index|[374, 376]|[336, 339]|351|346|346|passed-count-baseline|

## 失败项

无.

## 提醒与边界

- 没有recorder文件；用输入图、完整AUX及时间戳检查编译覆盖
- 自动结构、编号及实际PDF链接审计，不能代替逐页原文忠实性核对或最终PDF目视检查.
- 链接数量不足按失败报告；须逐页查真实引用，不能添加无关链接凑数.
- 数学源错误必须保留原编号和可见写法；本脚本不作数学纠错或正文改写.

完整输入图、编号期望、逐页链接计数、文件SHA256及具体失败上下文见同名JSON.
