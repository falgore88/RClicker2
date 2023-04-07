import copy
import json
import os

import settings
from core.rotation import Rotation
from libs.text import translate
from pathlib import Path

class Profile(object):
    PROFILE_DIR = settings.PROFILES_DIR

    BASE_STRUCTURE = {
        'name': '',
        'rotations': []
    }

    EXT = '.rclick'

    def __init__(self, profile_data):
        self._profile = profile_data

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Profile "{}": [{}]>'.format(str(self), ",".join(map(str, self.rotations)))

    def serialize(self):
        copy_profile = copy.deepcopy(self._profile)
        rotations = copy_profile.pop('rotations', [])
        copy_profile['rotations'] = []
        for r in rotations:
            copy_profile['rotations'].append(r.serialize())
        return json.dumps(copy_profile)

    @classmethod
    def deserialize(cls, data):
        parsed_profile = json.loads(data)
        profile = cls(parsed_profile)
        serialize_rotations = parsed_profile.pop('rotations', [])
        rotations = []
        for r in serialize_rotations:
            rotations.append(Rotation(profile, r))

        profile.set_rotations(rotations)
        return profile

    def set_rotations(self, rotations):
        self._profile['rotations'] = rotations

    @classmethod
    def load(cls, data):
        return cls.deserialize(data)

    def save(self):
        filename = self.get_profile_filename(self.name)
        with open(os.path.join(self.PROFILE_DIR, filename), 'w') as f:
            f.write(self.serialize())
        return filename

    @classmethod
    def get_profile_filename(cls, name):
        name = translate(name).lower().replace(' ', '_')
        return "{}{}".format(name, cls.EXT)

    @property
    def rotations(self):
        return self._profile.get('rotations', [])

    def add_rotation(self, rotation):
        self._profile['rotations'].append(rotation)

    def remove_rotation(self, rotation):
        self._profile['rotations'].remove(rotation)

    @property
    def name(self):
        return self._profile.get('name', '')

    @classmethod
    def create(cls, name):
        with open(os.path.join(cls.PROFILE_DIR, cls.get_profile_filename(name)), 'w') as f:
            profile_data = copy.deepcopy(cls.BASE_STRUCTURE)
            profile_data['name'] = name
            profile = Profile(profile_data)
            f.write(profile.serialize())
        return profile

    @classmethod
    def load_profiles(cls):
        profiles = []
        for file_name in os.listdir(cls.PROFILE_DIR):
            file_path = os.path.join(cls.PROFILE_DIR, file_name)
            if os.path.isfile(file_path):
                with open(file_path) as f:
                    profiles.append(cls.load(f.read()))
        return sorted(profiles, key=lambda p: p.name.lower())
