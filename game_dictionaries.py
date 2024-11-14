dict_game_forca = {
    "words": [
        "SUSTENTABILIDADE", "ENERGIA", "SOLAR", "EOLICA", "RENOVAVEL", 
        "BIODIESEL", "HIDRELETRICA", "BIOMASSA", "FOTOVOLTAICO", "GEOTERMICA",
        "EFICIENCIA", "CONSUMO", "DESCARBONIZACAO", "RECICLAGEM", "TERMICA",
        "SUSTENTAVEL", "ECOSSISTEMA", "CONSERVACAO", "INOVACAO", "BIODEGRADAVEL"
    ],
    
    "tips": [
        "Conceito que visa suprir necessidades atuais sem comprometer gerações futuras",
        "O que move o mundo e sustenta o modo de vida moderno",
        "Fonte de energia gerada a partir do sol",
        "Fonte de energia gerada a partir do vento",
        "Tipo de energia que não se esgota",
        "Combustível produzido a partir de fontes renováveis como óleos vegetais",
        "Fonte de energia gerada a partir da força da água",
        "Tipo de energia obtida a partir de matéria orgânica",
        "Tipo de energia que usa células para converter luz solar em eletricidade",
        "Energia que utiliza o calor da Terra como fonte",
        "Capacidade de fazer mais com menos energia",
        "Quantidade de energia usada por equipamentos ou sistemas",
        "Processo de reduzir emissões de gases de efeito estufa",
        "Processo de reaproveitamento de materiais descartados",
        "Energia gerada pela queima de combustíveis",
        "Relativo a práticas que minimizam impacto ambiental",
        "Conjunto de organismos que interagem entre si e com o ambiente",
        "Prática de manter e proteger recursos naturais",
        "Introdução de novas tecnologias e métodos sustentáveis",
        "Material que se decompõe naturalmente sem poluir o ambiente"
    ]
}

perguntas_quiz = {
    "Qual é a fonte de energia renovável mais utilizada no Brasil?": 
    (["A) Solar", "B) Eólica", "C) Hidrelétrica", "D) Biomassa", "E) Nuclear"], 2),
    
    "Qual gás é o maior responsável pelo efeito estufa?": 
    (["A) Metano", "B) Dióxido de carbono", "C) Óxido nitroso", "D) Vapor de água", "E) Ozônio"], 1),
    
    "Qual destes hábitos ajuda a economizar energia em casa?": 
    (["A) Deixar as luzes acesas", "B) Usar aparelhos durante horários de pico", "C) Manter aparelhos em standby", 
      "D) Usar lâmpadas LED", "E) Aumentar a potência dos aparelhos"], 3),
    
    "Qual é o benefício do uso de energia solar?": 
    (["A) Reduz custos de eletricidade", "B) Aumenta as emissões de CO₂", "C) Gasta muita água", 
      "D) Produz resíduos tóxicos", "E) Causa poluição sonora"], 0),
    
    "Qual dessas energias é considerada não renovável?": 
    (["A) Solar", "B) Hidrelétrica", "C) Carvão", "D) Eólica", "E) Biomassa"], 2),
    
    "Qual a principal desvantagem da energia eólica?": 
    (["A) Elevado custo de instalação", "B) Emissão de CO₂", "C) Causa poluição das águas", 
      "D) Intermitência do vento", "E) Necessita de combustíveis fósseis"], 3),
    
    "Qual é uma vantagem do uso de carros elétricos?": 
    (["A) Baixa eficiência energética", "B) Menor autonomia", "C) Maior emissão de CO₂", 
      "D) Alta dependência de petróleo", "E) Menos emissões de poluentes"], 4),
    
    "Qual dessas é uma forma de reduzir o consumo de energia elétrica?": 
    (["A) Usar lâmpadas incandescentes", "B) Reduzir o uso de ar-condicionado", 
      "C) Manter todos os aparelhos ligados", "D) Aumentar a potência dos aparelhos", 
      "E) Usar eletrodomésticos antigos"], 1),
    
    "Qual energia renovável depende do movimento da água?": 
    (["A) Solar", "B) Eólica", "C) Biomassa", "D) Hidrelétrica", "E) Geotérmica"], 3),
    
    "Qual destes é um efeito do aquecimento global?": 
    (["A) Diminuição do nível do mar", "B) Resfriamento global", "C) Extinção de espécies", 
      "D) Aumento das calotas polares", "E) Estabilização do clima"], 2),
}

desafios_consumo = [
    {
        "descricao": "Você está em casa em um dia quente. Como deseja refrescar o ambiente?",
        "opcoes": [
            ("Ventilador ligado por 2 horas", 0.5, 0.1),
            ("Ar-condicionado no modo econômico por 1 hora", 1.5, 0.3),
            ("Ar-condicionado no modo máximo por 1 hora", 3, 0.7)
        ]
    },
    {
        "descricao": "Você precisa iluminar a sala à noite. Qual opção você escolhe?",
        "opcoes": [
            ("Lâmpadas LED ligadas por 4 horas", 0.4, 0.05),
            ("Lâmpadas fluorescentes por 4 horas", 0.6, 0.1),
            ("Lâmpadas incandescentes por 4 horas", 1.2, 0.3)
        ]
    },
    {
        "descricao": "Na cozinha, você está preparando uma refeição. Qual fonte de aquecimento você usa?",
        "opcoes": [
            ("Fogão a gás", 1.0, 0.2),
            ("Forno elétrico por 30 minutos", 1.8, 0.4),
            ("Micro-ondas por 10 minutos", 0.5, 0.1)
        ]
    },
    {
        "descricao": "Você precisa lavar roupas. Como vai realizar essa tarefa?",
        "opcoes": [
            ("Máquina de lavar em modo econômico", 0.5, 0.1),
            ("Máquina de lavar em modo normal", 1.0, 0.2),
            ("Lavar a mão e secar ao sol", 0.0, 0.0)
        ]
    },
    {
        "descricao": "Você vai ao trabalho. Qual meio de transporte você escolhe?",
        "opcoes": [
            ("Bicicleta", 0.0, 0.0),
            ("Carro elétrico", 0.3, 0.05),
            ("Carro a combustão", 1.5, 0.3)
        ]
    }
]