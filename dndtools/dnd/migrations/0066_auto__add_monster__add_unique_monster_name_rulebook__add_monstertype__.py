# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Monster'
        db.create_table('dnd_monster', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rulebook', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dnd.Rulebook'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=32, db_index=True)),
            ('page', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dnd.RaceSize'], null=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dnd.MonsterType'])),
            ('hit_dice', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('initiative', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('armor_class', self.gf('django.db.models.fields.CharField')(default='32 (\xe2\x80\x931 size, +4 Dex, +19 natural)', max_length=128)),
            ('touch_armor_class', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('flat_footed_armor_class', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('base_attack', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('grapple', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('attack', self.gf('django.db.models.fields.CharField')(default='+3 greatsword +23 melee (3d6+13/19\xe2\x80\x9320) or slam +20 melee (2d8+10)', max_length=128)),
            ('full_attack', self.gf('django.db.models.fields.CharField')(default='+3 greatsword +23/+18/+13 melee (3d6+13/19\xe2\x80\x9320) or slam +20 melee (2d8+10)', max_length=128)),
            ('space', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('reach', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('special_attacks', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('special_qualities', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('fort_save', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('fort_save_extra', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('reflex_save', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('reflex_save_extra', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('will_save', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('will_save_extra', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('str', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('dex', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('con', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('int', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('wis', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cha', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('environment', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('challenge_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('treasure', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('alignment', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('advancement', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('level_adjustment', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('combat', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('combat_html', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('dnd', ['Monster'])

        # Adding M2M table for field subtypes on 'Monster'
        db.create_table('dnd_monster_subtypes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('monster', models.ForeignKey(orm['dnd.monster'], null=False)),
            ('monstersubtype', models.ForeignKey(orm['dnd.monstersubtype'], null=False))
        ))
        db.create_unique('dnd_monster_subtypes', ['monster_id', 'monstersubtype_id'])

        # Adding unique constraint on 'Monster', fields ['name', 'rulebook']
        db.create_unique('dnd_monster', ['name', 'rulebook_id'])

        # Adding model 'MonsterType'
        db.create_table('dnd_monstertype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=32, db_index=True)),
        ))
        db.send_create_signal('dnd', ['MonsterType'])

        # Adding model 'MonsterSpeed'
        db.create_table('dnd_monsterspeed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dnd.Monster'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['dnd.RaceSpeedType'])),
            ('speed', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('dnd', ['MonsterSpeed'])

        # Adding model 'MonsterSubtype'
        db.create_table('dnd_monstersubtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=32, db_index=True)),
        ))
        db.send_create_signal('dnd', ['MonsterSubtype'])

        # Changing field 'Race.con'
        db.alter_column('dnd_race', 'con', self.gf('django.db.models.fields.SmallIntegerField')(null=True))


    def backwards(self, orm):
        
        # Removing unique constraint on 'Monster', fields ['name', 'rulebook']
        db.delete_unique('dnd_monster', ['name', 'rulebook_id'])

        # Deleting model 'Monster'
        db.delete_table('dnd_monster')

        # Removing M2M table for field subtypes on 'Monster'
        db.delete_table('dnd_monster_subtypes')

        # Deleting model 'MonsterType'
        db.delete_table('dnd_monstertype')

        # Deleting model 'MonsterSpeed'
        db.delete_table('dnd_monsterspeed')

        # Deleting model 'MonsterSubtype'
        db.delete_table('dnd_monstersubtype')

        # Changing field 'Race.con'
        db.alter_column('dnd_race', 'con', self.gf('django.db.models.fields.SmallIntegerField')())


    models = {
        'dnd.characterclass': {
            'Meta': {'ordering': "['name']", 'object_name': 'CharacterClass'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'prestige': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'short_description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64', 'db_index': 'True'})
        },
        'dnd.characterclassvariant': {
            'Meta': {'unique_together': "(('character_class', 'rulebook'),)", 'object_name': 'CharacterClassVariant'},
            'advancement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'advancement_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'alignment': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'character_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.CharacterClass']"}),
            'class_features': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'class_features_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'class_skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.Skill']", 'symmetrical': 'False'}),
            'hit_die': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'required_bab': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'requirements': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'requirements_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rulebook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Rulebook']"}),
            'skill_points': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'dnd.characterclassvariantrequiresfeat': {
            'Meta': {'object_name': 'CharacterClassVariantRequiresFeat'},
            'character_class_variant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'required_feats'", 'to': "orm['dnd.CharacterClassVariant']"}),
            'extra': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Feat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dnd.characterclassvariantrequiresrace': {
            'Meta': {'object_name': 'CharacterClassVariantRequiresRace'},
            'character_class_variant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'required_races'", 'to': "orm['dnd.CharacterClassVariant']"}),
            'extra': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Race']"})
        },
        'dnd.characterclassvariantrequiresskill': {
            'Meta': {'object_name': 'CharacterClassVariantRequiresSkill'},
            'character_class_variant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'required_skills'", 'to': "orm['dnd.CharacterClassVariant']"}),
            'extra': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ranks': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Skill']"})
        },
        'dnd.dndedition': {
            'Meta': {'ordering': "['name']", 'object_name': 'DndEdition'},
            'core': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'system': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'dnd.domain': {
            'Meta': {'ordering': "['name']", 'object_name': 'Domain'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64', 'db_index': 'True'})
        },
        'dnd.feat': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'rulebook'),)", 'object_name': 'Feat'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'benefit_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'feat_categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.FeatCategory']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'normal': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'normal_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'page': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rulebook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Rulebook']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'special_feat_prerequisites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.SpecialFeatPrerequisite']", 'through': "orm['dnd.FeatSpecialFeatPrerequisite']", 'symmetrical': 'False'}),
            'special_html': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'dnd.featcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'FeatCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'})
        },
        'dnd.featrequiresfeat': {
            'Meta': {'object_name': 'FeatRequiresFeat'},
            'additional_text': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'required_feat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'required_by_feats'", 'to': "orm['dnd.Feat']"}),
            'source_feat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'required_feats'", 'to': "orm['dnd.Feat']"})
        },
        'dnd.featrequiresskill': {
            'Meta': {'object_name': 'FeatRequiresSkill'},
            'extra': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'required_skills'", 'to': "orm['dnd.Feat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Skill']"})
        },
        'dnd.featspecialfeatprerequisite': {
            'Meta': {'object_name': 'FeatSpecialFeatPrerequisite'},
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Feat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'special_feat_prerequisite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.SpecialFeatPrerequisite']"}),
            'value_1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'value_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        'dnd.monster': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'rulebook'),)", 'object_name': 'Monster'},
            'advancement': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'alignment': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'armor_class': ('django.db.models.fields.CharField', [], {'default': "'32 (\\xe2\\x80\\x931 size, +4 Dex, +19 natural)'", 'max_length': '128'}),
            'attack': ('django.db.models.fields.CharField', [], {'default': "'+3 greatsword +23 melee (3d6+13/19\\xe2\\x80\\x9320) or slam +20 melee (2d8+10)'", 'max_length': '128'}),
            'base_attack': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cha': ('django.db.models.fields.SmallIntegerField', [], {}),
            'challenge_rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'combat': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'combat_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'con': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dex': ('django.db.models.fields.SmallIntegerField', [], {}),
            'environment': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'flat_footed_armor_class': ('django.db.models.fields.SmallIntegerField', [], {}),
            'fort_save': ('django.db.models.fields.SmallIntegerField', [], {}),
            'fort_save_extra': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'full_attack': ('django.db.models.fields.CharField', [], {'default': "'+3 greatsword +23/+18/+13 melee (3d6+13/19\\xe2\\x80\\x9320) or slam +20 melee (2d8+10)'", 'max_length': '128'}),
            'grapple': ('django.db.models.fields.SmallIntegerField', [], {}),
            'hit_dice': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiative': ('django.db.models.fields.SmallIntegerField', [], {}),
            'int': ('django.db.models.fields.SmallIntegerField', [], {}),
            'level_adjustment': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'page': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reach': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'reflex_save': ('django.db.models.fields.SmallIntegerField', [], {}),
            'reflex_save_extra': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'rulebook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Rulebook']"}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.RaceSize']", 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'db_index': 'True'}),
            'space': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'special_attacks': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'special_qualities': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'str': ('django.db.models.fields.SmallIntegerField', [], {}),
            'subtypes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.MonsterSubtype']", 'symmetrical': 'False'}),
            'touch_armor_class': ('django.db.models.fields.SmallIntegerField', [], {}),
            'treasure': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.MonsterType']"}),
            'will_save': ('django.db.models.fields.SmallIntegerField', [], {}),
            'will_save_extra': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'wis': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'dnd.monsterspeed': {
            'Meta': {'object_name': 'MonsterSpeed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Monster']"}),
            'speed': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['dnd.RaceSpeedType']"})
        },
        'dnd.monstersubtype': {
            'Meta': {'object_name': 'MonsterSubtype'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'db_index': 'True'})
        },
        'dnd.monstertype': {
            'Meta': {'object_name': 'MonsterType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'db_index': 'True'})
        },
        'dnd.newsentry': {
            'Meta': {'ordering': "['-published']", 'object_name': 'NewsEntry'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_html': ('django.db.models.fields.TextField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'dnd.race': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'rulebook'),)", 'object_name': 'Race'},
            'cha': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'combat': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'combat_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'con': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dex': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'int': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'level_adjustment': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'page': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'racial_traits': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'racial_traits_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reach': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'}),
            'rulebook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Rulebook']"}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.RaceSize']", 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'db_index': 'True'}),
            'space': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'}),
            'str': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'wis': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'dnd.racefavoredcharacterclass': {
            'Meta': {'object_name': 'RaceFavoredCharacterClass'},
            'character_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.CharacterClass']"}),
            'extra': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'favored_classes'", 'to': "orm['dnd.Race']"})
        },
        'dnd.racesize': {
            'Meta': {'ordering': "['order']", 'object_name': 'RaceSize'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'dnd.racespeed': {
            'Meta': {'object_name': 'RaceSpeed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Race']"}),
            'speed': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['dnd.RaceSpeedType']"})
        },
        'dnd.racespeedtype': {
            'Meta': {'ordering': "['name', 'extra']", 'object_name': 'RaceSpeedType'},
            'extra': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'})
        },
        'dnd.rulebook': {
            'Meta': {'ordering': "['name']", 'object_name': 'Rulebook'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dnd_edition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.DndEdition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'official_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'dnd.skill': {
            'Meta': {'ordering': "['name']", 'object_name': 'Skill'},
            'armor_check_penalty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'base_skill': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'required_by_feats': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.Feat']", 'through': "orm['dnd.FeatRequiresSkill']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64', 'db_index': 'True'}),
            'trained_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dnd.skillvariant': {
            'Meta': {'unique_together': "(('skill', 'rulebook'),)", 'object_name': 'SkillVariant'},
            'action': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'action_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'check': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'check_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rulebook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Rulebook']"}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Skill']"}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'special_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'synergy': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'synergy_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'try_again': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'try_again_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'untrained': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'untrained_html': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'dnd.specialfeatprerequisite': {
            'Meta': {'ordering': "['name']", 'object_name': 'SpecialFeatPrerequisite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'print_format': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'dnd.spell': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'rulebook'),)", 'object_name': 'Spell'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'arcane_focus_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'casting_time': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'class_levels': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.CharacterClass']", 'through': "orm['dnd.SpellClassLevel']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descriptors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.SpellDescriptor']", 'symmetrical': 'False', 'blank': 'True'}),
            'divine_focus_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'domain_levels': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.Domain']", 'through': "orm['dnd.SpellDomainLevel']", 'symmetrical': 'False'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'extra_components': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta_breath_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'page': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'range': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'rulebook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Rulebook']"}),
            'saving_throw': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.SpellSchool']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'somatic_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'spell_resistance': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'sub_school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.SpellSubSchool']", 'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'true_name_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbal_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'xp_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dnd.spellclasslevel': {
            'Meta': {'ordering': "['spell', 'level']", 'unique_together': "(('character_class', 'spell'),)", 'object_name': 'SpellClassLevel'},
            'character_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.CharacterClass']"}),
            'extra': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'spell': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Spell']"})
        },
        'dnd.spelldescriptor': {
            'Meta': {'ordering': "['name']", 'object_name': 'SpellDescriptor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64', 'db_index': 'True'})
        },
        'dnd.spelldomainlevel': {
            'Meta': {'ordering': "['spell', 'level']", 'unique_together': "(('domain', 'spell'),)", 'object_name': 'SpellDomainLevel'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Domain']"}),
            'extra': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'spell': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Spell']"})
        },
        'dnd.spellschool': {
            'Meta': {'ordering': "['name']", 'object_name': 'SpellSchool'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'})
        },
        'dnd.spellsubschool': {
            'Meta': {'ordering': "['name']", 'object_name': 'SpellSubSchool'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'})
        },
        'dnd.staticpage': {
            'Meta': {'object_name': 'StaticPage'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'dnd.textfeatprerequisite': {
            'Meta': {'ordering': "['text']", 'object_name': 'TextFeatPrerequisite'},
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Feat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['dnd']
