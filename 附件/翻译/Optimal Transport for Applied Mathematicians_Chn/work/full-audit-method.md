# 全书最终审计脚本与实际执行

正式入口为`work/audit-full.py`。旧`audit_project.py`已改为兼容入口，转调全书脚本，取消仅第1章及94页的硬编码；`audit-progress.py`仅供历史预览，不作为全书完成判据。

脚本从MAIN递归展开真实input/include，核对前置7文件、8章及全部编号集合、69题与69提示、300书目和实际BibTeX顺序、163项/143主20子的完整makeindex索引。编号期望按各章原页独立清单固定，输入文件数、标签数、PDF页数及实际分段从最终文件获取。定义在MAIN宏中的sec:references/sec:index和sourcehint实例标签均识别；嵌套数学index参数采用花括号感知解析。

编译后读真实AUX/BBL/LOG/IDX/IND/ILG、PDF与源SHA256，检查新鲜度及构建/交付PDF字节一致。全书链接按底本376页拆前置、8章、题目、提示、书目和索引逐段核对，逐页计数保留。处理命名目标、直接Dest数组、URI与远程PDF，并对实际标签显示页和目标页作交叉核对。

第2章源PDF错链1条经原图、矩形和全章目标多重集合证实后单独排除，保留80→相关79的明确记录；重跑时重新对当前PDF验证其余79目标，而不是直接豁免。索引356出处在319目标落356个index；idx逐锚点shipout页、ind实际163词条、动态去重和页范围压缩后的hyperpage端点分别核对，避免把合法合并误判成缺漏或补假链接。

实际运行：首轮339页PDF发现真实前置错锚、两URI、obj1.26/4.41及box3.2/3.3目标页问题，交root统一局部修复；v2 SHA256 `bfba66983050819b33aa637ba86b626d5cd0b30ebf188be70d06a4703aa206c6` 重跑全量审计为0 failures。唯一方法提示是构建未生成.fls，因此以真实input图、完整AUX和文件时间戳核对编译覆盖。无旧94页结论沿用。manifest按实际通过的新审计更新。

另有`check_fidelity_project.py`按同一主输入图跑全量语言与结构扫描，154个proof和300引用键通过，记录`fidelity-static-full.json`；`audit-box-titles.py`从全339页实际标题字体文本运行检出43个框头，各唯一且目标同页，记录`box-title-destination-audit.md/json`。

这些自动检查不代替原页忠实性审阅或PDF实际看图。root维护的`fidelity-report.md`保留来源自审和独立cross；首轮339页已由团队分段实际看图；v2变化页按分工复看，并以PNG像素哈希承接未变化页，是否全段完成以各段实际报告和root汇总为准。脚本只写full-audit、静态、链接报告；只有显式传入`--write-manifest`且自动审计无失败时才更新manifest，不改TeX或索引数据。

## 最终v4实际结论

最终PDF仍339页，SHA256 `dbccdda368e058abba4fbf8a0a0cd75f2f6c33a41fba5cff7d4df33f6582c540`。v3标点排版曾使box7.2的锚留在前页，审计明确报失败，没有更新通过manifest；root加局部Needspace后v4重跑，全量audit-full为0失败，43框实际标题目标43/43同页，126个实际TOC项显示页/目标页全部一致。manifest、编号、链接及静态报告均已更新到该最终SHA。131–230的100张最终PNG与v2实看完成状态逐个字节SHA一致，最终承接记录已保存。
