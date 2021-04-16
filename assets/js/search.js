
  var lunrIndex = null;
  var lunrLookup = null;

  async function lunrSearch(term)
  {

   term = term.trim();
    if (!term)
      return;

    if (lunrIndex)
    {
      const raw_results = lunrIndex.search(term);
      let results = []
      for (var result of raw_results)
      {
        var doc = lunrLookup[result.ref];

        results.push({
          'uri':doc.uri,
          'title':doc.title,
          'summary':lunrTruncate(doc.content,30)
        })
      }
      return results
    }
  }

  function lunrTruncate(text, minWords)
  {
    var match;
    var result = "";
    var wordCount = 0;
    var regexp = /(\S+)(\s*)/g;
    while (match = regexp.exec(text))
    {
      wordCount++;
      if (wordCount <= minWords)
        result += match[0];
      else
      {
        var char1 = match[1][match[1].length - 1];
        var char2 = match[2][0];
        if (/[.?!"]/.test(char1) || char2 == "\n")
        {
          result += match[1];
          break;
        }
        else
          result += match[0];
      }
    }
    return result;
  }

  function initLunrIndex()
  {
    var request = new XMLHttpRequest();
    request.open("GET", "/search.json");
    request.responseType = "json";
    request.addEventListener("load", function(event)
    {
      
      lunrLookup = {};
      lunrIndex = lunr(function()
      {

       
        // code to use a lunr language pack.

        this.pipeline.remove(lunr.stemmer)
        this.searchPipeline.remove(lunr.stemmer)
        //this.use(lunr.fr);

        this.ref("uri");
        this.field("title");
        this.field("tags");
        this.field("designations")
        this.field("catalogs")
    
        for (var doc of request.response)
        {
          this.add(doc);
          lunrLookup[doc.uri] = doc;
        }

        
      });
    }, false);
    request.send(null);
  }
