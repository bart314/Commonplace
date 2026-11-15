# The Commonplace

# Inleiding
Dit project is geboren uit een kleine frustratie. Ik maak erg veel onderwijsmateriaal, en meestal gebruik ik daar [mkdocs]() voor. Op zich een prima framework, maar je merkt wel dat het primair gemaakt is voor technische documentatie: het is erg tekstueel gedreven, heeft veel opties voor code en LaTeX en ik niet heel erg mobile first.

Het materiaal wat ik ontwikkeld zit op een ander, meer creatief vlak. Veel voorbeelden in de vorm van afbeeldingen en video's en citaten op verschillende plaatsen. Verder wil ik kleine lees- en kijkopdrachten snel kunnen afwisselen met kleine practische oefeningen en reflecties. Zeker in deze  tijd en in het domein waarin ik opereer is het van belang korte en snelle informatie te verschaffen. Dat kan allemaal wel in mkdocs, maar je moet er best veel werk in steken.

## Opbouw
*The Commonplace* is bewust heel simpel van opzet: er is een directory `frameworks/templates`, waarin html-bestanden staan met onderdelen (gekenmerkt door `{{` en `}}`) die door het framework worden gevuld. Deze onderdelen worden gevuld door markdown-bestanden die in de `src`-directory staan.

Specifiek kent *The Commonplace* een opbouw in weken – het is immers primair een onderwijs-framework. Elke week bestaat uit meerdere markdown-bestanden die ofwel een leesopdracht ofwel een praktische oefening bevatten. Deze oefeningen worden als *tegels* op de index-pagina van de betreffende week weergegeven.

De opbouw van de website is gegeven in het bestand `website.yaml` in de *root* van het project. De individuele weken staan dan weer als tegels in de index van het project zelf.


## Legal
Omdat elke onderwijsmodule ook een onderdeeltje 'regels en beoordelingssystematiek' heeft, voorziet het framework daar ook in. Hiervoor worden onder de week-tegels op de hoofdpagina de 'legal'-tegels gezet. Hier komt de inhoud in die in de markdown-bestanden in `src/legal/` is opgeslagen en die wordt opgezet volgens de specs in `website.yaml`.