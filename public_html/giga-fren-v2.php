<?php include("count.php"); ?>
<!DOCTYPE html
	PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
	 "http://www.w3.org/TR/html4/loose.dtd">
<html><head><title>giga-fren</title>
<link rev="made" href="mailto:Joerg%20Tiedemann">

<meta name="robots" content="NOFOLLOW">
<link rel="stylesheet" type="text/css" href="index.css">
</head>
<body>
<div class="header"><?php include("header.php"); ?></div><h1>giga-fren</h1>Giga-word corpus for French-English from  <a href="http://www.statmt.org/wmt10/translation-task.html">WMT2010</a> collected by <a href="http://www.cis.upenn.edu/~ccb/">Chris Callison-Burch</a><p>2 languages, total number of files: 452<br>total number of tokens: 1.43G<br>total number of sentence fragments: 47.55M<br><p>Please <a href="http://opus.lingfil.uu.se/LREC2012.txt">cite the following article</a> if you use any part of the corpus in your own work:<br/> J. Tiedemann, 2012, <a href="http://www.lrec-conf.org/proceedings/lrec2012/pdf/463_Paper.pdf"><i>Parallel Data, Tools and Interfaces in OPUS.</i></a> In Proceedings of the 8th International Conference on Language Resources and Evaluation (LREC 2012)<br/><h3>Download</h3><p>Below you can download data files for all language pairs in different formats and with different kind of annotation (if available). You can click on the various links as explained below. In addition to the files shown on this webpage, OPUS also provides pre-compiled word alignments and phrase tables, bilingual dictionaries, frequency counts, and these files can be found through the <a href="/index.php">resources search form on the top-level website of OPUS</a>. <table><tr><td>Bottom-left triangle: download files<ul><li><i>ces</i> = sentence alignments in XCES format</li> <li><i>leftmost column language IDs</i> = tokenized corpus files in XML</li> <li>TMX and plain text files (Moses): see "Statistics" below</li> <li><i>lower row language IDs</i> = parsed corpus files (if they exist)</li></ul></td><td>Upper-right triangle: sample files <ul><li><i>view</i> = bilingual XML file samples</li> <li><i>upper row language IDs</i> = monolingual XML file samples</li> <li><i>rightmost column language IDs</i> = untokenized corpus files</li></ul></td></tr></table><p><div class="sample"><table border="0" cellpadding="0">
<tr>
<th></th>
<th><a rel="nofollow" href="giga-fren/v2/en_sample.html">en</a></th>
<th><a rel="nofollow" href="giga-fren/v2/fr_sample.html">fr</a></th>
<th></th></tr>
<tr><th><a rel="nofollow" href="download.php?f=giga-fren/v2/xml/en.zip">en</a></th>
<th></th>
<td><a rel="nofollow" title="English-French (sample file)" href="giga-fren/v2/en-fr_sample.html">view</a></td><th><a rel="nofollow" href="download.php?f=giga-fren/v2/raw/en.zip">en</a></th></tr>
<tr><th><a rel="nofollow" href="download.php?f=giga-fren/v2/xml/fr.zip">fr</a></th>
<td><a rel="nofollow" title="sentence alignments for 'French-English' (226 aligned documents, 22.5M links, 1.4G tokens)" href="download.php?f=giga-fren/v2/xml/en-fr.xml.gz">ces</a></td>
<th></th>
<th><a rel="nofollow" href="download.php?f=giga-fren/v2/raw/fr.zip">fr</a></th></tr>
<tr><th></th>
<th>en</th>
<th>fr</th>
<th></th></tr>
</table>
</div><p><h3>Statistics and TMX/Moses Downloads</h3>Number of files, tokens, and sentences per language (including non-parallel ones if they exist)<br>Number of sentence alignment units per language pair<p>Upper-right triangle: download translation memory files (TMX)<br>Bottom-left triangle: download plain text files (MOSES/GIZA++)<br>Language ID's, first row: monolingual plain text files (tokenized)<br>Language ID's, first column: monolingual plain text files (untokenized)<div class="counts"><table><caption></caption> <tr><th>language</th> <th>files</th> <th>tokens</th> <th>sentences</th><th><a rel="nofollow" title='monolingual tokenized en plain text' href="download.php?f=giga-fren/v2/mono/giga-fren.en.gz">en</a>
</th><th><a rel="nofollow" title='monolingual tokenized fr plain text' href="download.php?f=giga-fren/v2/mono/giga-fren.fr.gz">fr</a>
</th></tr> <tr><th><a rel="nofollow" title='monolingual untokenized en plain text' href="download.php?f=giga-fren/v2/mono/giga-fren.raw.en.gz">en</a>
</th><td>226</td> <td>653.0M</td> <td>23.7M</td><td></td><td bgcolor="#bfffbf"><a rel="nofollow" title='English-French (21,858,378 sentence pairs, 1.21G words) - TMX format' href="download.php?f=giga-fren/v2/tmx/en-fr.tmx.gz">21.9M</a>
</td></tr> <tr><th><a rel="nofollow" title='monolingual untokenized fr plain text' href="download.php?f=giga-fren/v2/mono/giga-fren.raw.fr.gz">fr</a>
</th><td>226</td> <td>781.6M</td> <td>23.8M</td><td bgcolor="#bfffbf"><a rel="nofollow" title='French-English (22,519,904 sentence pairs, 1.25G words) - Moses format' href="download.php?f=giga-fren/v2/moses/en-fr.txt.zip">22.5M</a>
</td><td></td></tr></table></div><p>Note that TMX files only contain unique translation units and, therefore, the number of aligned units is smaller than for the distributions in Moses and XML format. Moses downloads include all non-empty alignment units including duplicates. Token counts for each language also include duplicate sentences and documents.<p><hr><div class="footer"></div>
</body>
</html>