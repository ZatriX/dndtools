# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TextFeatPrerequisite'
        db.create_table('dnd_textfeatprerequisite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Feat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dnd.Feat'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('dnd', ['TextFeatPrerequisite'])

        # Adding model 'FeatSpecialFeatPrerequisite'
        db.create_table('dnd_featspecialfeatprerequisite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dnd.Feat'])),
            ('special_feat_prerequisite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dnd.SpecialFeatPrerequisite'])),
            ('value_1', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('value_2', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('dnd', ['FeatSpecialFeatPrerequisite'])

        # Adding model 'SpecialFeatPrerequisite'
        db.create_table('dnd_specialfeatprerequisite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('print_format', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('dnd', ['SpecialFeatPrerequisite'])

        # Adding M2M table for field feat_categories on 'Feat'
        db.create_table('dnd_feat_feat_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feat', models.ForeignKey(orm['dnd.feat'], null=False)),
            ('featcategory', models.ForeignKey(orm['dnd.featcategory'], null=False))
        ))
        db.create_unique('dnd_feat_feat_categories', ['feat_id', 'featcategory_id'])

        # Adding M2M table for field requiredFeats on 'Feat'
        db.create_table('dnd_feat_requiredFeats', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_feat', models.ForeignKey(orm['dnd.feat'], null=False)),
            ('to_feat', models.ForeignKey(orm['dnd.feat'], null=False))
        ))
        db.create_unique('dnd_feat_requiredFeats', ['from_feat_id', 'to_feat_id'])

        # Adding M2M table for field requiredSkills on 'Feat'
        db.create_table('dnd_feat_requiredSkills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('feat', models.ForeignKey(orm['dnd.feat'], null=False)),
            ('skill', models.ForeignKey(orm['dnd.skill'], null=False))
        ))
        db.create_unique('dnd_feat_requiredSkills', ['feat_id', 'skill_id'])

        # Adding unique constraint on 'Feat', fields ['rulebook', 'name']
        db.create_unique('dnd_feat', ['rulebook_id', 'name'])

        # Adding unique constraint on 'FeatCategory', fields ['name']
        db.create_unique('dnd_featcategory', ['name'])

        # Adding unique constraint on 'Skill', fields ['rulebook', 'name']
        db.create_unique('dnd_skill', ['rulebook_id', 'name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Skill', fields ['rulebook', 'name']
        db.delete_unique('dnd_skill', ['rulebook_id', 'name'])

        # Removing unique constraint on 'FeatCategory', fields ['name']
        db.delete_unique('dnd_featcategory', ['name'])

        # Removing unique constraint on 'Feat', fields ['rulebook', 'name']
        db.delete_unique('dnd_feat', ['rulebook_id', 'name'])

        # Deleting model 'TextFeatPrerequisite'
        db.delete_table('dnd_textfeatprerequisite')

        # Deleting model 'FeatSpecialFeatPrerequisite'
        db.delete_table('dnd_featspecialfeatprerequisite')

        # Deleting model 'SpecialFeatPrerequisite'
        db.delete_table('dnd_specialfeatprerequisite')

        # Removing M2M table for field feat_categories on 'Feat'
        db.delete_table('dnd_feat_feat_categories')

        # Removing M2M table for field requiredFeats on 'Feat'
        db.delete_table('dnd_feat_requiredFeats')

        # Removing M2M table for field requiredSkills on 'Feat'
        db.delete_table('dnd_feat_requiredSkills')


    models = {
        'dnd.characterclass': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'rulebook'),)", 'object_name': 'CharacterClass'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'page': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prestige': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rulebook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Rulebook']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'})
        },
        'dnd.dndedition': {
            'Meta': {'ordering': "['name']", 'object_name': 'DndEdition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'db_index': 'True'}),
            'system': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'dnd.domain': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'rulebook'),)", 'object_name': 'Domain'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'page': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rulebook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Rulebook']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'})
        },
        'dnd.feat': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'rulebook'),)", 'object_name': 'Feat'},
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'feat_categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.FeatCategory']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'normal': ('django.db.models.fields.TextField', [], {}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'page': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'requiredFeats': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'requiredForFeats'", 'symmetrical': 'False', 'to': "orm['dnd.Feat']"}),
            'requiredSkills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.Skill']", 'symmetrical': 'False'}),
            'rulebook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Rulebook']"}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'special': ('django.db.models.fields.TextField', [], {}),
            'specialFeatPrerequisites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.SpecialFeatPrerequisite']", 'through': "orm['dnd.FeatSpecialFeatPrerequisite']", 'symmetrical': 'False'})
        },
        'dnd.featcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'FeatCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'db_index': 'True'})
        },
        'dnd.featspecialfeatprerequisite': {
            'Meta': {'object_name': 'FeatSpecialFeatPrerequisite'},
            'feat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Feat']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'special_feat_prerequisite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.SpecialFeatPrerequisite']"}),
            'value_1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'value_2': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'dnd.rulebook': {
            'Meta': {'ordering': "['name']", 'object_name': 'Rulebook'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dnd_edition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.DndEdition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'official_url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'dnd.skill': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'rulebook'),)", 'object_name': 'Skill'},
            'action': ('django.db.models.fields.TextField', [], {}),
            'armor_check_penalty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'base_skill': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'check': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'rulebook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Rulebook']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'db_index': 'True'}),
            'special': ('django.db.models.fields.TextField', [], {}),
            'synergy': ('django.db.models.fields.TextField', [], {}),
            'trained_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'try_again': ('django.db.models.fields.TextField', [], {}),
            'untrained': ('django.db.models.fields.TextField', [], {})
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
            'descriptors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.SpellDescriptor']", 'symmetrical': 'False'}),
            'divine_focus_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'domain_levels': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dnd.Domain']", 'through': "orm['dnd.SpellDomainLevel']", 'symmetrical': 'False'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
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
            'verbal_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'xp_component': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dnd.spellclasslevel': {
            'Meta': {'ordering': "['spell', 'level']", 'unique_together': "(('character_class', 'spell'),)", 'object_name': 'SpellClassLevel'},
            'character_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.CharacterClass']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'spell': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Spell']"})
        },
        'dnd.spelldescriptor': {
            'Meta': {'ordering': "['name']", 'object_name': 'SpellDescriptor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'})
        },
        'dnd.spelldomainlevel': {
            'Meta': {'ordering': "['spell', 'level']", 'unique_together': "(('domain', 'spell'),)", 'object_name': 'SpellDomainLevel'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Domain']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'spell': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Spell']"})
        },
        'dnd.spellschool': {
            'Meta': {'ordering': "['name']", 'object_name': 'SpellSchool'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'db_index': 'True'})
        },
        'dnd.spellsubschool': {
            'Meta': {'ordering': "['name']", 'object_name': 'SpellSubSchool'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32', 'db_index': 'True'})
        },
        'dnd.textfeatprerequisite': {
            'Feat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dnd.Feat']"}),
            'Meta': {'ordering': "['text']", 'object_name': 'TextFeatPrerequisite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['dnd']
