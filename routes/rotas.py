from flask import request, jsonify

from database.sessao import db
from model.produto import Produto

def rotasGerais(app):
    
    @app.route("/cadastrar/produto", methods=["POST"])
    def criarProduto():
        data = request.get_json()

        if not data.get('nome') and not data.get('valor') and not data.get('codigoBarras'):
            return jsonify({'mensagem':'Erro ao criar: Requisição sem corpo json.'}), 400

        if Produto.query.filter_by(codigoBarras=data['codigoBarras']).first(): 
            return jsonify({"error": "Produto com o mesmo código de barras já cadastrado."}), 409
        
        if Produto.query.filter_by(etiqueta=data['etiqueta']).first(): 
            return jsonify({"error": "Produto com a mesma etiqueta já cadastrada."}), 409
        
        #teste
        nome = data['nome'].title()

        if type(data["etiqueta"]) != int and type(data["codigoBarras"]) != int: 
            return jsonify({'Error': 'Etiqueta e Codigo de Barras devem ser numeros inteiros'}), 409
        if data["etiqueta"] >= 10:
            return jsonify({'Error': 'Não temos tantas etiquetas, o máximo são 9'}), 409
        
        novoProduto = Produto(
            nome = nome,
            valor = data['valor'],
            codigoBarras = data["codigoBarras"],
            etiqueta = data["etiqueta"],
            descricao = data.get("descricao", None)
        )

        db.session.add(novoProduto)
        db.session.commit()

        return jsonify({'mensagem':'Produto cadastrado com sucesso'}), 201
    
    @app.route("/listar/produto", methods=["GET"])
    def listarProdutos():
        produtos = Produto.query.all()

        resultados = []
        for produto in produtos: 
            item = {
                'id': produto.id,
                'nome': produto.nome,
                'valor': produto.valor,
                'codigoBarras': produto.codigoBarras,
                'etiqueta': produto.etiqueta,
                'descricao': produto.descricao
            }
            resultados.append(item)
        
        return jsonify(resultados), 200
    
    @app.route("/filtro/produto", methods=["GET"])
    def filtrarProduto():
        etiqueta = request.args.get('etiqueta')
        codigoBarras = request.args.get('codigoBarras')
        query = Produto.query

        if not codigoBarras and not etiqueta:
            return jsonify({'error':"Parametros 'id' ou 'codigoBarras' é necessario."}), 404
        
        if codigoBarras:
            query = query.filter_by(codigoBarras=codigoBarras)
        if etiqueta:
            query = query.filter_by(etiqueta=etiqueta)
        
        items = query.all()
        produtos = []
        for produto in items:
            item = {
                'id': produto.id,
                'nome': produto.nome,
                'valor': produto.valor,
                'codigoBarras': produto.codigoBarras,
                'Descricao': produto.descricao,
                'Etiqueta': produto.etiqueta
            }
            produtos.append(item)

        if not produtos: return jsonify({'error':"Produto nao encontrado."}), 404

        return jsonify(produtos), 200

    @app.route("/atualizar/produto", methods=["PUT"])
    def atualizarProduto():

        def prod(produto, data):
            if not produto:
                return jsonify({'error':'Produto não encontrado'}), 404

            produto.nome = data.get('nome', produto.nome).title()
            produto.valor = data.get('valor', produto.valor)
            produto.descricao = data.get('descricao', produto.descricao)
            produto.etiqueta = data.get('etiqueta', produto.etiqueta)

            db.session.commit()

        codigoBarras = request.args.get('codigoBarras')
        etiqueta = request.args.get('etiqueta')
        
        if not codigoBarras and not etiqueta:
            return jsonify({'error': 'Parâmetro "codigoBarras" ou "etiqueta" ausentes'}), 400
        
        data = request.get_json()

        if not data:
            return jsonify({'error': 'Requisição sem dados'}), 400
        
        if type(data["etiqueta"]) != int and type(data["codigoBarras"]) != int: 
            return jsonify({'Error': 'Etiqueta e Codigo de Barras devem ser numeros inteiros'}), 409
        if data["etiqueta"] >= 10:
            return jsonify({'Error': 'Não temos tantas etiquetas, o máximo são 9'}), 409

        prodEtiqueta = Produto.query.filter_by(etiqueta=data.get('etiqueta')).first()
        if prodEtiqueta:
            prodEtiqueta.etiqueta = 0
            db.session.commit()

        if etiqueta:
            produtoEtiqueta = Produto.query.filter_by(etiqueta=etiqueta).first()
            prod(produtoEtiqueta, data)
            return jsonify({'message':'Produto atualizado com sucesso'}), 200
        if codigoBarras:
            prodCodigo = Produto.query.filter_by(codigoBarras=codigoBarras).first()
            prod(prodCodigo, data)
            return jsonify({'message':'Produto atualizado com sucesso'}), 200

    @app.route("/deletar/produto", methods=["DELETE"])
    def deletarProduto():
        codigoBarras = request.args.get('codigoBarras')

        if not codigoBarras:
            return jsonify({'error': 'Parâmetro "codigoBarras" ausente'}), 400
        
        produto = Produto.query.filter_by(codigoBarras=codigoBarras).first()

        if not produto:
            return jsonify({'error':'Produto não encontrado'}), 404

        db.session.delete(produto)
        db.session.commit()

        return jsonify({"message": "Produto deletado com sucesso"}), 200