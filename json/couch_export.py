
import couchdb
import json

class BerserkerJsonExport:
    def __init__(self):
        self.config_file = 'BerserkerJsonExportConfig'
        self.cfg = __import__(self.config_file)
        self.server = couchdb.Server(self.cfg.BERSERKER_SERVER)
        try:
            self.server.delete(self.cfg.BERSERKER_DATABASE)
            self.server.create(self.cfg.BERSERKER_DATABASE)
        except CouchError:
            pass
        self.db = self.server[self.cfg.BERSERKER_DATABASE]
        self.ITEM_FILES = ['Armor.json', 'Items.json', 'Weapons.json']
        self.LANGUAGE_FILES = ['English.json']
    def export_items(self):
        print 'Read each local json file'
        json_files = ['Armor.json', 'Items.json', 'Weapons.json', 'StoryDefault.json', 'English.json']
        for f in json_files:
            in_file = json.load(open(f,'r'))
            print 'Create unique id for each type in json files'
            if f in self.ITEM_FILES:
                for item in in_file:
                    item['_id'] = 'base_' + item['object_type'] + '_' + item['name'].replace(' ', '_')
                self.db.update(in_file) 
            elif f == 'StoryDefault.json':
                story_name = 'unknown'
                # Need to delete placeholder strings in the json file because cloudant will crash
                # if we try an update with them.  Python hates mutable lists though so we create a
                # new one.
                result = []
                for item in in_file:
                    object_type = None
                    try:
                        object_type = item['object_type']
                    except (KeyError, TypeError):
                        continue
                    if object_type == 'story':
                        story_name = item['short_name']
                        item['_id'] = 'story_' + story_name
                    result.append(item)
                for item in result:
                    if item.get('_id') is None:
                        item['_id'] = story_name + '_' + item['object_type'] + '_' + item['name'].replace(' ', '_')
                self.db.update(result)
            elif f in self.LANGUAGE_FILES:
                pass
                #for item Iin in_file:
                #    item`
                #self.db.update(in_file)
            print 'Push {} new document to cloudant'.format(f)


if __name__ == "__main__":
    exporter = BerserkerJsonExport()
    exporter.export_items()

