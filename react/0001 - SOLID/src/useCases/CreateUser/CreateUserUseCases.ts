import { User } from "../../entities/User";
import { IMailProvider } from "../../providers/IMailProvider";
import { IUserRepository } from "../../repositories/IUserRepository";
import { ICreateUserRequestDTO } from "./CreateUserDTO";

export class CreateUserUseCase{

    constructor(
        private usersRepository: IUserRepository,
        private mailProvider: IMailProvider
    ){}

    async execute(data: ICreateUserRequestDTO){
        const userAlreadyExists = await this.usersRepository.findByEmail(data.email);

        if (userAlreadyExists){
            throw new Error('Usuário já existe!')
        }

        const user = new User(data);

        await this.usersRepository.save(user);

        await this.mailProvider.sendMail({
            to: {
                name: data.name,
                email: data.email
            },
            from: {
                name: 'Equipe Desenvolvimento',
                email: 'equipe@email.com'
            },
            subject: 'Seja bem vindo!',
            body: '<p>Você já pode logar na sua conta!</p>'
        })
    }
}