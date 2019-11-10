# puddletag：音频标签编辑工具
- ubuntu,metadata,media,
- 2015-03-06 07:05:31

这个软件功能比较强大，可以修改各种 Tag。因为项目需要，我需要修改 Media File 的 Metadata 信息，但是 Ubuntu 上的播放器啥的都不能修改音乐文件的信息，所以找到了这个软件。下面是官方网站的一些介绍。

## What it is

下面的介绍来自官方网站，http://puddletag.sourceforge.net/index.html  ，更新的介绍请访问官方网站。

> puddletag is an audio tag editor (primarily created) for GNU/Linux similar to the Windows program, Mp3tag. Unlike most taggers for GNU/Linux, it uses a spreadsheet-like layout so that all the tags you want to edit by hand are visible and easily editable.

> The usual tag editor features are supported like extracting tag information from filenames, renaming files based on their tags by using patterns and basic tag editing.

> Then there’re Functions, which can do things like replace text, trim it, do case conversions, etc. Actions can automate repetitive tasks. You can import your QuodLibet library, lookup tags using Amazon (including cover art), Discogs (does cover art too!), FreeDB and MusicBrainz. There’s quite a bit more, but I’ve reached my comma quota.

> Supported formats: ID3v1, ID3v2 (mp3), MP4 (mp4, m4a, etc.), VorbisComments (ogg, flac), Musepack (mpc), Monkey’s Audio (.ape) and WavPack (wv).

http://puddletag.sourceforge.net/index.html

## 安装：

    sudo add-apt-repository ppa:webupd8team/puddletag
    sudo apt-get update
    sudo apt-get install puddletag
