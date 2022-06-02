from voluptuous import PREVENT_EXTRA, Schema, All, Length

InfoResponseSchema = Schema(
    {'classes': All([str], Length(min=1)),
     'factions': All([str], Length(min=1)),
     'locales': {'DE_DE': str,
                 'EN_GB': str,
                 'EN_US': str,
                 'ES_ES': str,
                 'ES_MX': str,
                 'FR_FR': str,
                 'IT_IT': str,
                 'JA_JP': str,
                 'KO_KR': str,
                 'PL_PL': str,
                 'PT_BR': str,
                 'RU_RU': str,
                 'TH_TH': str,
                 'ZH_CN': str,
                 'ZH_TW': str},
     'patch': str,
     'qualities': All([str], Length(min=1)),
     'races': All([str], Length(min=1)),
     'sets': All([str], Length(min=1)),
     'standard': All([str], Length(min=1)),
     'types': All([str], Length(min=1)),
     'wild': All([str], Length(min=1))},
    extra=PREVENT_EXTRA,
    required=True
)

InfoErrorResponseSchema = Schema(
    {'message': str},
    extra=PREVENT_EXTRA,
    required=True
)
