#!/usr/bin/env bash
#.pngtmp作为备用目录,以及活动更新图片目录,不参与仓库同步
if [ ! -d .pngtmp ]; then mkdir -p .pngtmp; fi
mv assets/* .pngtmp/
for pyfile in $(ls *py)
do
for i in $(grep -Eo 'tpl[[:alnum:]_]*.png' $pyfile)
do
cp .pngtmp/$i assets/
done
done