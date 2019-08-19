




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>sortphotos/src/sortphotos.py at master · andrewning/sortphotos · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="andrewning/sortphotos" name="twitter:title" /><meta content="sortphotos - SortPhotos is a Python script that organizes photos into folders using date/time information" name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/2747412?s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/2747412?s=400" property="og:image" /><meta content="andrewning/sortphotos" property="og:title" /><meta content="https://github.com/andrewning/sortphotos" property="og:url" /><meta content="sortphotos - SortPhotos is a Python script that organizes photos into folders using date/time information" property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector-new.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="56B05F8A:4761:765632D:539778DF" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico" />


    <meta content="authenticity_token" name="csrf-param" />
<meta content="bsD0FQ7zkX9HEHBXT/TR7gNynS5r7VE8nJcOV0eOJf0SIZMjknWukO1wc9rKosOX5XzTxd1mYbsTGPmGqCtKGw==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-2a5fe476db9a69ca883f024853575d588b2bd187.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-a1fd2161b2d8ea3aef1c3d15c79772ff80eb5523.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="cc9167eb91e25e1e59deba1003934246">

      
  <meta name="description" content="sortphotos - SortPhotos is a Python script that organizes photos into folders using date/time information" />

  <meta content="2747412" name="octolytics-dimension-user_id" /><meta content="andrewning" name="octolytics-dimension-user_login" /><meta content="8596686" name="octolytics-dimension-repository_id" /><meta content="andrewning/sortphotos" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="8596686" name="octolytics-dimension-repository_network_root_id" /><meta content="andrewning/sortphotos" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/andrewning/sortphotos/commits/master.atom" rel="alternate" title="Recent Commits to sortphotos:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production macintosh vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Fandrewning%2Fsortphotos%2Fblob%2Fmaster%2Fsrc%2Fsortphotos.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s, /" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="andrewning/sortphotos"
      data-branch="master"
      data-sha="40cf09e7b5feb8e175a2b2ce4ccc3e71735f48ee"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="andrewning/sortphotos" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
    <a href="/login?return_to=%2Fandrewning%2Fsortphotos"
    class="minibutton with-count star-button tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>Star
  </a>

    <a class="social-count js-social-count" href="/andrewning/sortphotos/stargazers">
      25
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fandrewning%2Fsortphotos"
        class="minibutton with-count js-toggler-target fork-button tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>Fork
      </a>
      <a href="/andrewning/sortphotos/network" class="social-count">
        14
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/andrewning" class="url fn" itemprop="url" rel="author"><span itemprop="title">andrewning</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/andrewning/sortphotos" class="js-current-repository js-repo-home-link">sortphotos</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/andrewning/sortphotos" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /andrewning/sortphotos">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/andrewning/sortphotos/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues /andrewning/sortphotos/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/andrewning/sortphotos/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /andrewning/sortphotos/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/andrewning/sortphotos/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /andrewning/sortphotos/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/andrewning/sortphotos/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /andrewning/sortphotos/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/andrewning/sortphotos/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /andrewning/sortphotos/network">
          <span class="octicon octicon-repo-forked"></span> <span class="full-word">Network</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/andrewning/sortphotos.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/andrewning/sortphotos.git" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/andrewning/sortphotos" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/andrewning/sortphotos" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>

  <a href="http://mac.github.com" data-url="github-mac://openRepo/https://github.com/andrewning/sortphotos" class="minibutton sidebar-button js-conduit-rewrite-url" title="Save andrewning/sortphotos to your computer and use it in GitHub Desktop." aria-label="Save andrewning/sortphotos to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>


                <a href="/andrewning/sortphotos/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download andrewning/sortphotos as a zip file"
                   title="Download andrewning/sortphotos as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<a href="/andrewning/sortphotos/blob/fdf4058ecd74c2fe75c521b17514d2cdbb49d776/src/sortphotos.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:95323b6f2db259cd3ff8cad43d84b77b -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/andrewning/sortphotos/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/andrewning/sortphotos/blob/master/src/sortphotos.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/andrewning/sortphotos" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">sortphotos</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/andrewning/sortphotos/tree/master/src" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">src</span></a></span><span class="separator"> / </span><strong class="final-path">sortphotos.py</strong> <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="src/sortphotos.py" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>
</div>


  <div class="commit file-history-tease">
      <img alt="andrewning" class="main-avatar js-avatar" data-user="2747412" height="24" src="https://avatars2.githubusercontent.com/u/2747412?s=140" width="24" />
      <span class="author"><a href="/andrewning" rel="author">andrewning</a></span>
      <time datetime="2014-05-03T23:24:28-06:00" is="relative-time">May 03, 2014</time>
      <div class="commit-title">
          <a href="/andrewning/sortphotos/commit/18dce90e911a2c1b6f688ff8ec6c366c083df2d8" class="message" data-pjax="true" title="flexible directory structures for sorting!  fixes #7">flexible directory structures for sorting! fixes</a> <a href="https://github.com/andrewning/sortphotos/issues/7" class="issue-link" title="Let user customize the folder architecture.">#7</a>
      </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>3</strong>  contributors</a></p>
          <a class="avatar tooltipped tooltipped-s" aria-label="andrewning" href="/andrewning/sortphotos/commits/master/src/sortphotos.py?author=andrewning"><img alt="andrewning" class=" js-avatar" data-user="2747412" height="20" src="https://avatars2.githubusercontent.com/u/2747412?s=140" width="20" /></a>
    <a class="avatar tooltipped tooltipped-s" aria-label="cedricbou" href="/andrewning/sortphotos/commits/master/src/sortphotos.py?author=cedricbou"><img alt="cedricbou" class=" js-avatar" data-user="1747280" height="20" src="https://avatars0.githubusercontent.com/u/1747280?s=140" width="20" /></a>
    <a class="avatar tooltipped tooltipped-s" aria-label="hmashlah" href="/andrewning/sortphotos/commits/master/src/sortphotos.py?author=hmashlah"><img alt="Hazem Mashlah" class=" js-avatar" data-user="1911336" height="20" src="https://avatars0.githubusercontent.com/u/1911336?s=140" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="andrewning" class=" js-avatar" data-user="2747412" height="24" src="https://avatars2.githubusercontent.com/u/2747412?s=140" width="24" />
            <a href="/andrewning">andrewning</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="cedricbou" class=" js-avatar" data-user="1747280" height="24" src="https://avatars0.githubusercontent.com/u/1747280?s=140" width="24" />
            <a href="/cedricbou">cedricbou</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Hazem Mashlah" class=" js-avatar" data-user="1911336" height="24" src="https://avatars0.githubusercontent.com/u/1911336?s=140" width="24" />
            <a href="/hmashlah">hmashlah</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">executable file</span>
        <span class="meta-divider"></span>
          <span>277 lines (190 sloc)</span>
          <span class="meta-divider"></span>
        <span>8.776 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
            <a class="minibutton tooltipped tooltipped-w js-conduit-openfile-check"
               href="http://mac.github.com"
               data-url="github-mac://openRepo/https://github.com/andrewning/sortphotos?branch=master&amp;filepath=src%2Fsortphotos.py"
               aria-label="Open this file in GitHub for Mac"
               data-failed-title="Your version of GitHub for Mac is too old to open this file. Try checking for updates.">
                <span class="octicon octicon-device-desktop"></span> Open
            </a>
              <a class="minibutton disabled tooltipped tooltipped-w" href="#"
                 aria-label="You must be signed in to make or propose changes">Edit</a>
          <a href="/andrewning/sortphotos/raw/master/src/sortphotos.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/andrewning/sortphotos/blame/master/src/sortphotos.py" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/andrewning/sortphotos/commits/master/src/sortphotos.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div class="blob-wrapper data type-python js-blob-data">
       <table class="file-code file-diff tab-size-8">
         <tr class="file-code-line">
           <td class="blob-line-nums">
             <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>

           </td>
           <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><span class="c"># encoding: utf-8</span></div><div class='line' id='LC3'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC4'><span class="sd">sortphotos.py</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="sd">Created on 3/2/2013</span></div><div class='line' id='LC7'><span class="sd">Copyright (c) S. Andrew Ning. All rights reserved.</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC10'><br/></div><div class='line' id='LC11'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC12'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC13'><span class="kn">import</span> <span class="nn">shutil</span></div><div class='line' id='LC14'><span class="kn">import</span> <span class="nn">fnmatch</span></div><div class='line' id='LC15'><span class="kn">import</span> <span class="nn">subprocess</span></div><div class='line' id='LC16'><span class="kn">import</span> <span class="nn">filecmp</span></div><div class='line' id='LC17'><span class="kn">from</span> <span class="nn">datetime</span> <span class="kn">import</span> <span class="n">datetime</span><span class="p">,</span> <span class="n">timedelta</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><span class="kn">import</span> <span class="nn">exifread</span></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><br/></div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'><span class="c"># -------- convenience methods -------------</span></div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'><span class="k">def</span> <span class="nf">parse_date_exif</span><span class="p">(</span><span class="n">date_string</span><span class="p">):</span></div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC28'><span class="sd">    extract date info from EXIF data</span></div><div class='line' id='LC29'><span class="sd">    YYYY:MM:DD HH:MM:SS</span></div><div class='line' id='LC30'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC31'><br/></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elements</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">date_string</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">date_entries</span> <span class="o">=</span> <span class="n">elements</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">year</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">date_entries</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">month</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">date_entries</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">day</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">date_entries</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span></div><div class='line' id='LC38'><br/></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time_entries</span> <span class="o">=</span> <span class="n">elements</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">hour</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">time_entries</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">minute</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">time_entries</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">second</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">time_entries</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span></div><div class='line' id='LC44'><br/></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">hour</span> <span class="o">=</span> <span class="mi">12</span>  <span class="c"># defaulting to noon if no time data provided</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">minute</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">second</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC49'><br/></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">datetime</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">day</span><span class="p">,</span> <span class="n">hour</span><span class="p">,</span> <span class="n">minute</span><span class="p">,</span> <span class="n">second</span><span class="p">)</span></div><div class='line' id='LC51'><br/></div><div class='line' id='LC52'><br/></div><div class='line' id='LC53'><span class="k">def</span> <span class="nf">parse_date_tstamp</span><span class="p">(</span><span class="n">fname</span><span class="p">):</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;extract date info from file timestamp&quot;&quot;&quot;</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># time of last modification</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="s">&#39;nt&#39;</span><span class="p">:</span>  <span class="c"># windows allows direct access to creation date</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">creation_time</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">getctime</span><span class="p">(</span><span class="n">fname</span><span class="p">)</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">creation_time</span> <span class="o">=</span> <span class="n">get_creation_time</span><span class="p">(</span><span class="n">fname</span><span class="p">)</span></div><div class='line' id='LC61'><br/></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">creation_time</span><span class="p">)</span></div><div class='line' id='LC63'><br/></div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'><span class="k">def</span> <span class="nf">check_for_early_morning_photos</span><span class="p">(</span><span class="n">date</span><span class="p">,</span> <span class="n">day_begins</span><span class="p">):</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;check for early hour photos to be grouped with previous day&quot;&quot;&quot;</span></div><div class='line' id='LC67'><br/></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">date</span><span class="o">.</span><span class="n">hour</span> <span class="o">&lt;</span> <span class="n">day_begins</span><span class="p">:</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">date</span> <span class="o">=</span> <span class="n">date</span> <span class="o">-</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">hours</span><span class="o">=</span><span class="n">date</span><span class="o">.</span><span class="n">hour</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span>  <span class="c"># push it to the day before for classificiation purposes</span></div><div class='line' id='LC70'><br/></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">date</span></div><div class='line' id='LC72'><br/></div><div class='line' id='LC73'><br/></div><div class='line' id='LC74'><span class="k">def</span> <span class="nf">valid_date</span><span class="p">(</span><span class="n">date</span><span class="p">):</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;check if date is not zero time and matches correct EXIF format: YYYY:MM:DD HH:MM:SS&quot;&quot;&quot;</span></div><div class='line' id='LC76'><br/></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">elements</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">date</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">))</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">date_entries</span> <span class="o">=</span> <span class="n">elements</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">valid_date</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">date_entries</span><span class="p">)</span> <span class="o">==</span> <span class="mi">3</span> <span class="ow">and</span> <span class="n">date_entries</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">&gt;</span> <span class="s">&#39;0000&#39;</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">valid_time</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC84'><br/></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">valid_time</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">))</span> <span class="o">==</span> <span class="mi">3</span></div><div class='line' id='LC87'><br/></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">valid_date</span> <span class="ow">and</span> <span class="n">valid_time</span></div><div class='line' id='LC89'><br/></div><div class='line' id='LC90'><br/></div><div class='line' id='LC91'><span class="c"># Courtesy of Alec Thomas (http://stackoverflow.com/questions/36932/whats-the-best-way-to-implement-an-enum-in-python)</span></div><div class='line' id='LC92'><span class="k">def</span> <span class="nf">enum</span><span class="p">(</span><span class="o">*</span><span class="n">sequential</span><span class="p">,</span> <span class="o">**</span><span class="n">named</span><span class="p">):</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">enums</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">sequential</span><span class="p">,</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">sequential</span><span class="p">))),</span> <span class="o">**</span><span class="n">named</span><span class="p">)</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="s">&#39;Enum&#39;</span><span class="p">,</span> <span class="p">(),</span> <span class="n">enums</span><span class="p">)</span></div><div class='line' id='LC95'><br/></div><div class='line' id='LC96'><br/></div><div class='line' id='LC97'><span class="c"># Modification of --&gt; Miles (http://stackoverflow.com/questions/946967/get-file-creation-time-with-python-on-mac)</span></div><div class='line' id='LC98'><span class="k">def</span> <span class="nf">get_creation_time</span><span class="p">(</span><span class="n">path</span><span class="p">):</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;linux&#39;</span><span class="p">):</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flag</span> <span class="o">=</span> <span class="s">&#39;-c %Y&#39;</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span>  <span class="c"># OS X</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flag</span> <span class="o">=</span> <span class="s">&#39;-f %B&#39;</span></div><div class='line' id='LC103'><br/></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">p</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">([</span><span class="s">&#39;stat&#39;</span><span class="p">,</span> <span class="n">flag</span><span class="p">,</span> <span class="n">path</span><span class="p">],</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">stdout</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span> <span class="n">stderr</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">)</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">p</span><span class="o">.</span><span class="n">wait</span><span class="p">():</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">OSError</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">rstrip</span><span class="p">())</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">read</span><span class="p">())</span></div><div class='line' id='LC110'><br/></div><div class='line' id='LC111'><span class="c"># ---------------------------------------</span></div><div class='line' id='LC112'><br/></div><div class='line' id='LC113'><br/></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'><br/></div><div class='line' id='LC116'><span class="c"># --------- main script -----------------</span></div><div class='line' id='LC117'><br/></div><div class='line' id='LC118'><span class="k">def</span> <span class="nf">sortPhotos</span><span class="p">(</span><span class="n">src_dir</span><span class="p">,</span> <span class="n">dest_dir</span><span class="p">,</span> <span class="n">extensions</span><span class="p">,</span> <span class="n">sort_format</span><span class="p">,</span> <span class="n">move_files</span><span class="p">,</span> <span class="n">removeDuplicates</span><span class="p">,</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ignore_exif</span><span class="p">,</span> <span class="n">day_begins</span><span class="p">):</span></div><div class='line' id='LC120'><br/></div><div class='line' id='LC121'><br/></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># some error checking</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">src_dir</span><span class="p">):</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&#39;Source directory does not exist&#39;</span><span class="p">)</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">dest_dir</span><span class="p">):</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&#39;Destination directory does not exist&#39;</span><span class="p">)</span></div><div class='line' id='LC127'><br/></div><div class='line' id='LC128'><br/></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># find files that have the specified extensions</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matched_files</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC131'><br/></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># check if file system is case sensitive</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">case_sensitive_os</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normcase</span><span class="p">(</span><span class="s">&#39;A&#39;</span><span class="p">)</span> <span class="o">==</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">normcase</span><span class="p">(</span><span class="s">&#39;a&#39;</span><span class="p">):</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">case_sensitive_os</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC136'><br/></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># recurvsively search directory</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">root</span><span class="p">,</span> <span class="n">dirnames</span><span class="p">,</span> <span class="n">filenames</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">walk</span><span class="p">(</span><span class="n">src_dir</span><span class="p">):</span></div><div class='line' id='LC139'><br/></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># search for all files that match the extension</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">ext</span> <span class="ow">in</span> <span class="n">extensions</span><span class="p">:</span></div><div class='line' id='LC142'><br/></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># grab both upper and lower case matches if necessary</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matches</span> <span class="o">=</span> <span class="n">fnmatch</span><span class="o">.</span><span class="n">filter</span><span class="p">(</span><span class="n">filenames</span><span class="p">,</span> <span class="s">&#39;*.&#39;</span> <span class="o">+</span> <span class="n">ext</span><span class="o">.</span><span class="n">lower</span><span class="p">())</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">case_sensitive_os</span><span class="p">:</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matches</span> <span class="o">+=</span> <span class="n">fnmatch</span><span class="o">.</span><span class="n">filter</span><span class="p">(</span><span class="n">filenames</span><span class="p">,</span> <span class="s">&#39;*.&#39;</span> <span class="o">+</span> <span class="n">ext</span><span class="o">.</span><span class="n">upper</span><span class="p">())</span></div><div class='line' id='LC147'><br/></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># add file root and save the matched file in list</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">match</span> <span class="ow">in</span> <span class="n">matches</span><span class="p">:</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">matched_files</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">match</span><span class="p">))</span></div><div class='line' id='LC151'><br/></div><div class='line' id='LC152'><br/></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># setup a progress bar</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">num_files</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">matched_files</span><span class="p">)</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">idx</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC156'><br/></div><div class='line' id='LC157'><br/></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">src_file</span> <span class="ow">in</span> <span class="n">matched_files</span><span class="p">:</span></div><div class='line' id='LC159'><br/></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># update progress bar</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">numdots</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="mf">20.0</span><span class="o">*</span><span class="p">(</span><span class="n">idx</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">/</span><span class="n">num_files</span><span class="p">)</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\r</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;[</span><span class="si">%-20s</span><span class="s">] </span><span class="si">%d</span><span class="s"> of </span><span class="si">%d</span><span class="s"> &#39;</span> <span class="o">%</span> <span class="p">(</span><span class="s">&#39;=&#39;</span><span class="o">*</span><span class="n">numdots</span><span class="p">,</span> <span class="n">idx</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span> <span class="n">num_files</span><span class="p">))</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div><div class='line' id='LC165'><br/></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">idx</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">ignore_exif</span><span class="p">:</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">date</span> <span class="o">=</span> <span class="n">parse_date_tstamp</span><span class="p">(</span><span class="n">src_file</span><span class="p">)</span></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># open file</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">src_file</span><span class="p">,</span> <span class="s">&#39;rb&#39;</span><span class="p">)</span></div><div class='line' id='LC174'><br/></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tags</span> <span class="o">=</span> <span class="n">exifread</span><span class="o">.</span><span class="n">process_file</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">details</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC176'><br/></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC178'><br/></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># look for date in EXIF data</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;EXIF DateTimeOriginal&#39;</span> <span class="ow">in</span> <span class="n">tags</span> <span class="ow">and</span> <span class="n">valid_date</span><span class="p">(</span><span class="n">tags</span><span class="p">[</span><span class="s">&#39;EXIF DateTimeOriginal&#39;</span><span class="p">]):</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">date</span> <span class="o">=</span> <span class="n">parse_date_exif</span><span class="p">(</span><span class="n">tags</span><span class="p">[</span><span class="s">&#39;EXIF DateTimeOriginal&#39;</span><span class="p">])</span></div><div class='line' id='LC182'><br/></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="s">&#39;EXIF DateTimeDigitized&#39;</span> <span class="ow">in</span> <span class="n">tags</span> <span class="ow">and</span> <span class="n">valid_date</span><span class="p">(</span><span class="n">tags</span><span class="p">[</span><span class="s">&#39;EXIF DateTimeDigitized&#39;</span><span class="p">]):</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">date</span> <span class="o">=</span> <span class="n">parse_date_exif</span><span class="p">(</span><span class="n">tags</span><span class="p">[</span><span class="s">&#39;EXIF DateTimeDigitized&#39;</span><span class="p">])</span></div><div class='line' id='LC185'><br/></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="s">&#39;Image DateTime&#39;</span> <span class="ow">in</span> <span class="n">tags</span> <span class="ow">and</span> <span class="n">valid_date</span><span class="p">(</span><span class="n">tags</span><span class="p">[</span><span class="s">&#39;Image DateTime&#39;</span><span class="p">]):</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">date</span> <span class="o">=</span> <span class="n">parse_date_exif</span><span class="p">(</span><span class="n">tags</span><span class="p">[</span><span class="s">&#39;Image DateTime&#39;</span><span class="p">])</span></div><div class='line' id='LC188'><br/></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span>  <span class="c"># use file time stamp if no valid EXIF data</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">date</span> <span class="o">=</span> <span class="n">parse_date_tstamp</span><span class="p">(</span><span class="n">src_file</span><span class="p">)</span></div><div class='line' id='LC191'><br/></div><div class='line' id='LC192'><br/></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># early morning photos can be grouped with previous day (depending on user setting)</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">date</span> <span class="o">=</span> <span class="n">check_for_early_morning_photos</span><span class="p">(</span><span class="n">date</span><span class="p">,</span> <span class="n">day_begins</span><span class="p">)</span></div><div class='line' id='LC195'><br/></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># create folder structure</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dir_structure</span> <span class="o">=</span> <span class="n">date</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="n">sort_format</span><span class="p">)</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dirs</span> <span class="o">=</span> <span class="n">dir_structure</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest_file</span> <span class="o">=</span> <span class="n">dest_dir</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">thedir</span> <span class="ow">in</span> <span class="n">dirs</span><span class="p">:</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest_file</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">dest_file</span><span class="p">,</span> <span class="n">thedir</span><span class="p">)</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">dest_file</span><span class="p">):</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">dest_file</span><span class="p">)</span></div><div class='line' id='LC204'><br/></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># setup destination file</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest_file</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">dest_file</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">src_file</span><span class="p">))</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">root</span><span class="p">,</span> <span class="n">ext</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">dest_file</span><span class="p">)</span></div><div class='line' id='LC208'><br/></div><div class='line' id='LC209'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># check for collisions</span></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">append</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fileIsIdentical</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC212'><br/></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="bp">True</span><span class="p">:</span></div><div class='line' id='LC214'><br/></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">dest_file</span><span class="p">):</span>  <span class="c"># check for existing name</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">removeDuplicates</span> <span class="ow">and</span> <span class="n">filecmp</span><span class="o">.</span><span class="n">cmp</span><span class="p">(</span><span class="n">src_file</span><span class="p">,</span> <span class="n">dest_file</span><span class="p">):</span>  <span class="c"># check for identical files</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fileIsIdentical</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC219'><br/></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span>  <span class="c"># name is same, but file is different</span></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dest_file</span> <span class="o">=</span> <span class="n">root</span> <span class="o">+</span> <span class="s">&#39;_&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">append</span><span class="p">)</span> <span class="o">+</span> <span class="n">ext</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">append</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC223'><br/></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC226'><br/></div><div class='line' id='LC227'><br/></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># finally move or copy the file</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">move_files</span><span class="p">:</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">src_file</span><span class="p">,</span> <span class="n">dest_file</span><span class="p">)</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">fileIsIdentical</span><span class="p">:</span></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span>  <span class="c"># if file is same, we just ignore it (for copy option)</span></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shutil</span><span class="o">.</span><span class="n">copy2</span><span class="p">(</span><span class="n">src_file</span><span class="p">,</span> <span class="n">dest_file</span><span class="p">)</span></div><div class='line' id='LC236'><br/></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span></div><div class='line' id='LC239'><br/></div><div class='line' id='LC240'><br/></div><div class='line' id='LC241'><br/></div><div class='line' id='LC242'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC243'><br/></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">argparse</span></div><div class='line' id='LC245'><br/></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># setup command line parsing</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">(</span><span class="n">formatter_class</span><span class="o">=</span><span class="n">argparse</span><span class="o">.</span><span class="n">RawTextHelpFormatter</span><span class="p">,</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">description</span><span class="o">=</span><span class="s">&#39;Sort files (primarily photos) into folders by date</span><span class="se">\n</span><span class="s">using EXIF data if possible and file creation date if not&#39;</span><span class="p">)</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;src_dir&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&#39;source directory (searched recursively)&#39;</span><span class="p">)</span></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;dest_dir&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&#39;destination directory&#39;</span><span class="p">)</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;-m&#39;</span><span class="p">,</span> <span class="s">&#39;--move&#39;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&#39;move files instead of copy&#39;</span><span class="p">)</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;-s&#39;</span><span class="p">,</span> <span class="s">&#39;--sort&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s">&#39;%Y/%m-%b&#39;</span><span class="p">,</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&quot;choose destination folder structure using datetime format </span><span class="se">\n\</span></div><div class='line' id='LC254'><span class="s">https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior. </span><span class="se">\n\</span></div><div class='line' id='LC255'><span class="s">Use forward slashes / to indicate subdirectory(ies) (independent of your OS convention). </span><span class="se">\n\</span></div><div class='line' id='LC256'><span class="s">The default is &#39;</span><span class="si">%%</span><span class="s">Y/</span><span class="si">%%</span><span class="s">m-</span><span class="si">%%</span><span class="s">b&#39;, which separates by year then month </span><span class="se">\n\</span></div><div class='line' id='LC257'><span class="s">with both the month number and name (e.g., 2012/12-Feb).&quot;</span><span class="p">)</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;--keep-duplicates&#39;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;If file is a duplicate keep it anyway (after renmaing).&#39;</span><span class="p">)</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;--extensions&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span> <span class="n">nargs</span><span class="o">=</span><span class="s">&#39;+&#39;</span><span class="p">,</span></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">default</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;jpg&#39;</span><span class="p">,</span> <span class="s">&#39;jpeg&#39;</span><span class="p">,</span> <span class="s">&#39;tiff&#39;</span><span class="p">,</span> <span class="s">&#39;arw&#39;</span><span class="p">,</span> <span class="s">&#39;avi&#39;</span><span class="p">,</span> <span class="s">&#39;mov&#39;</span><span class="p">,</span> <span class="s">&#39;mp4&#39;</span><span class="p">,</span> <span class="s">&#39;mts&#39;</span><span class="p">],</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;file types to sort&#39;</span><span class="p">)</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;--ignore-exif&#39;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">help</span><span class="o">=</span><span class="s">&#39;always use file time stamp even if EXIF data exists&#39;</span><span class="p">)</span></div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s">&#39;--day-begins&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&#39;hour of day that new day begins (0-23), </span><span class="se">\n\</span></div><div class='line' id='LC266'><span class="s">defaults to 0 which corresponds to midnight.  Useful for grouping pictures with previous day.&#39;</span><span class="p">)</span></div><div class='line' id='LC267'><br/></div><div class='line' id='LC268'><br/></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># parse command line arguments</span></div><div class='line' id='LC270'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span></div><div class='line' id='LC271'><br/></div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sortPhotos</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">src_dir</span><span class="p">,</span> <span class="n">args</span><span class="o">.</span><span class="n">dest_dir</span><span class="p">,</span> <span class="n">args</span><span class="o">.</span><span class="n">extensions</span><span class="p">,</span> <span class="n">args</span><span class="o">.</span><span class="n">sort</span><span class="p">,</span></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">args</span><span class="o">.</span><span class="n">move</span><span class="p">,</span> <span class="ow">not</span> <span class="n">args</span><span class="o">.</span><span class="n">keep_duplicates</span><span class="p">,</span> <span class="n">args</span><span class="o">.</span><span class="n">ignore_exif</span><span class="p">,</span> <span class="n">args</span><span class="o">.</span><span class="n">day_begins</span><span class="p">)</span></div><div class='line' id='LC274'><br/></div><div class='line' id='LC275'><br/></div><div class='line' id='LC276'><br/></div></pre></div></td>
         </tr>
       </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.03364s from github-fe126-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x close js-ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-c044173f1e759e8299dbe414ec8ed23e4405bdc5.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-abafbb1b61823e40063e9f65128096bcfef3b025.js" type="text/javascript"></script>
      
      
        <script async src="https://www.google-analytics.com/analytics.js"></script>
  </body>
</html>

